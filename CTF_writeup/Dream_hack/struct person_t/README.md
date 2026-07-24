# 1. Find Bug :

<img width="2559" height="801" alt="image" src="https://github.com/user-attachments/assets/1004b068-3222-4bb7-9acd-8bcc3daee6de" />

- Buffer overflow ở hàm `sub_40123A(nation, 128)` do trong đó có hàm `read` với 2 tham số truyền vào :

<img width="1014" height="211" alt="image" src="https://github.com/user-attachments/assets/14774e42-5112-42ad-af95-3fa8575ab6b1" />

- Và ở bên trái ta thấy có hàm `sub_401216` chạy `execve`

<img width="1483" height="596" alt="image" src="https://github.com/user-attachments/assets/6166df0f-99d4-4e88-b66f-b98e5797a21b" />

# 2. Idea :

- Tìm cách leak & bypass `canary`

- Overwrite saved RIP -> `sub_401216`

# 3. Exploit :

<img width="2559" height="1516" alt="image" src="https://github.com/user-attachments/assets/365973b1-77ac-4620-94d7-85508c6afd26" />

- Trước hết ta thấy file bị stripped

- PIE tắt -> Có thể hardcore thẳng địa chỉ hàm `sub_401216`

<img width="1269" height="643" alt="image" src="https://github.com/user-attachments/assets/28e97f08-33b5-40f6-a5a7-92d16c035a58" />

- Ở hàm `sub_40123A` : Nếu kí tự cuối là `\n` -> `\0` -> Nếu ta nhập full size sẽ ko dính `\0`

-> Để leak canary ta nhập full size `name`, nhập số thật lớn cho `age` và `height` để ko dính NULL byte, và quan trọng nhất là 5 byte ở `&age + 4` để nối thẳng tới `canary` 

<img width="780" height="325" alt="image" src="https://github.com/user-attachments/assets/8bd666cd-2683-4d89-a5af-e914756f65e0" />

-------------------------------

<img width="2555" height="1583" alt="image" src="https://github.com/user-attachments/assets/87f75650-4b80-4601-a4a6-20745ce69cd3" />

- Sau `DEBUG` ta thấy canary đã chuẩn giờ tiếp theo là overwrite saved RIP -> `sub_401216`

<img width="2558" height="1097" alt="image" src="https://github.com/user-attachments/assets/aef35671-468d-4c40-b3dd-681ede1cc78a" />

- Vào `ida` ta có thể thấy nó ở địa chỉ `0x0000000000401216`

- `canary` có, `địa chỉ cần overwrite` có -> tính offset từ `nation` đến `saved RIP` là xong

<img width="722" height="201" alt="image" src="https://github.com/user-attachments/assets/ffbeb30d-f90f-4cd4-9348-cebe28ba0b3a" />

## SCRIPT :

<img width="1017" height="1376" alt="image" src="https://github.com/user-attachments/assets/8c4f43b3-4b3e-49ff-99ac-7d7d8e3487fa" />

# 4. Get Flag :

<img width="1158" height="277" alt="image" src="https://github.com/user-attachments/assets/40b9b791-7c7f-4551-81d0-353f44fbb47f" />
