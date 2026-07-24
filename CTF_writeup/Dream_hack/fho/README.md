# 1. Find Bug :

<img width="2553" height="932" alt="image" src="https://github.com/user-attachments/assets/b0e84ca5-0cd0-402f-b17a-f2bd32f0a200" />

- BOF ở hàm `read`

- `free(ptr)` -> tận dụng __free_hook

# 2. Idea :

<img width="547" height="206" alt="image" src="https://github.com/user-attachments/assets/1b2ea208-25f5-4105-85cf-6ab1f37b02ea" />

- `*ptr = v5` và được nhập cả 2 -> Overwrite `__free_hook` thành `target address`

# 3. Exploit :

- STAGE 1 : LEAK LIBC

  <img width="2556" height="997" alt="image" src="https://github.com/user-attachments/assets/c573f48d-d5e2-4ce8-8a14-052a0ea013a7" />

  + Leak `libc start main` với padding đã tính toán là `72` nhờ BOF và hàm `printf("Buf: %s\n", buf)`

  <img width="805" height="279" alt="image" src="https://github.com/user-attachments/assets/0cba6863-75a7-42ac-8166-06848d74b4cc" />
  ---------------------------------
  <img width="1714" height="623" alt="image" src="https://github.com/user-attachments/assets/f8a86a83-fb20-482b-8fd2-5cdf39345618" />

  + Sau khi có libc_leak -> libc_base

- STAGE 2 : Overwrite GOT

  + Với việc có libc_base -> Dùng `one_gadget`

  <img width="2324" height="753" alt="image" src="https://github.com/user-attachments/assets/5d30e3be-ed1c-474c-aaba-8dc4bc45b40f" />

  + `target address` = `libc_base` + `offset` ( Thử lần lượt các offset ở one_gadget)

  <img width="1008" height="116" alt="image" src="https://github.com/user-attachments/assets/31161e66-73f3-4c81-8933-682ed108a9d2" />

# 4. Get Flag :

<img width="1533" height="293" alt="image" src="https://github.com/user-attachments/assets/8d83ea24-9caf-4880-8eb9-ec0a35b62cfe" />
