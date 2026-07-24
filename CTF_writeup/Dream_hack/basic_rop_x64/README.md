# 1. Find bug :

<img width="2499" height="759" alt="image" src="https://github.com/user-attachments/assets/f5dfa8fe-936a-4eda-bc12-cbedaf8fa6a1" />

- Lỗi buffer overflow ở hàm read

# 2. Idea :

- Ở ida nhìn bên trái ko có hàm win hay gì để get shell luôn

- <img width="1732" height="288" alt="image" src="https://github.com/user-attachments/assets/575d357b-8e24-48e2-8cf2-588cc0223f3c" />

- Dùng checksec thấy NX bật -> ko r2shellcode được

- <img width="2357" height="130" alt="image" src="https://github.com/user-attachments/assets/1e06841f-5147-45f3-b2e3-545cc73fbf84" />

- Do ko thấy pop rdx, rax, syscall nên khả năng ko ROPchain thuần được

------> Dùng r2libc

# 3. Exploit :

- <img width="2410" height="1005" alt="image" src="https://github.com/user-attachments/assets/ff939e25-c094-4ac2-8e77-e3cb469b985c" />

- Ta tìm được offset để overwrite saved RIP là 72

- Tiếp theo là tìm `libc leak`

- <img width="1275" height="340" alt="image" src="https://github.com/user-attachments/assets/8e4aaf05-4b84-403f-8714-ca7acfad993b" />

--> Leak `GOT read` bằng hàm puts

<img width="980" height="302" alt="image" src="https://github.com/user-attachments/assets/a6a4b8a8-23d9-4cb0-ae48-50b9931c5579" />

- Do hàm write trả về 64byte nên phải nhận trước 64 byte rồi đến 6byte cuối là `libc leak`, đồng thời thêm 2byte NULL để đủ 8byte để u64 hợp lệ

- Remote sever local để xem libc leak của sever rồi lên `libc.rip` tải bản thử các bản

- Tiếp theo là pwninit để patch file binary + libc

- <img width="880" height="125" alt="image" src="https://github.com/user-attachments/assets/66491aa3-02c6-4244-b1c9-32ba70d63c27" />

- Tìm `libc base` = `libc_leak - libc.sym.read`

- <img width="1055" height="165" alt="image" src="https://github.com/user-attachments/assets/23c22b46-9381-4a3c-b0b9-75b389c7f396" />

- Sau khi về `main` thì lại viết thêm payload chạy hàm system

- <img width="2559" height="1177" alt="image" src="https://github.com/user-attachments/assets/0aaa44db-d33b-409d-88eb-ca2cf52d50e2" />

- ## Lưu ý : Sau debug với payload tạm thời như vậy sẽ dính xmm đặc trưng do ko chia hết 16 ---> Giải pháp ở đây là thêm `p64(ret)`

- ### SCRIPT:

- <img width="1134" height="1369" alt="image" src="https://github.com/user-attachments/assets/610c3b56-7e2e-4e07-abc8-92f9dc9c68f3" />

# 4. Get Flag :

<img width="1533" height="124" alt="image" src="https://github.com/user-attachments/assets/2565baa3-62df-4d62-b804-0adf0bf84da3" />
