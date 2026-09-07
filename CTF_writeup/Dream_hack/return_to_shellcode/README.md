# 1. Find Bug :

<img width="1879" height="733" alt="image" src="https://github.com/user-attachments/assets/c2e2949d-65e9-4011-be76-beb8cd1ee48d" />

- Leak address buf, distance buf & $rbp

- Buffer overflow ở hàm `read`, `gets`

# 2. Idea :

<img width="1417" height="244" alt="image" src="https://github.com/user-attachments/assets/7b08422b-0561-4054-9cad-37a0998d66db" />

- NX off -> r2shellcode

- PIE bật -> cần leak, nhưng bài này cho sẵn địa chỉ buf 

- Stage 1 : Leak canary

- Stage 2 : Gửi shellcode và overwrite return address -> shellcode

# 3. Exploit :

<img width="729" height="112" alt="image" src="https://github.com/user-attachments/assets/4012d1b4-b684-4f64-bd69-addee2ff31df" />

----------------

<img width="971" height="280" alt="image" src="https://github.com/user-attachments/assets/f637a1cd-59b5-4770-9962-e70f3ce988d7" />

## - Trước hết, lấy địa chỉ buf mà chương trình leak

<img width="506" height="226" alt="image" src="https://github.com/user-attachments/assets/953aff48-bc13-4136-8ede-2360cf4055df" />

-----------------

<img width="2559" height="645" alt="image" src="https://github.com/user-attachments/assets/63c01128-3193-47f7-b4d2-f25c221c08c3" />

- Leak canary, đồng thời check bằng `gdb.attach` luôn

- LƯU Ý : Vì canary luôn có `NULL Byte` ở cuối nên dùng `sla` cho hàm `read` thay vì `sa` như thông thường để có `\n(0a)` nối chuỗi 7 byte còn lại của canary -> Sau khi nhận 88 byte 'A' cũng phải nhận thêm `1byte` để skip `0a` -> Để hoàn chỉnh canary phải nhận thêm `NULL byte` ở đầu khi u64

<img width="777" height="586" alt="image" src="https://github.com/user-attachments/assets/c2dbbb0e-0ae9-4c4f-ac76-0d6844c0dc25" />

- Viết shellcode và overwrite return address -> shellcode

- LƯU Ý : Ở chỗ `sub rbp, 0x200`, vì một lí do nào đó nếu chạy ko có cái này `local` thì được nhưng lên `sever` lại ko được, có thể do `rsp % 16 phải == 0` nên phải thêm dòng này để `sever` được

- HOẶC có thêm 1 cách khác : dùng `shellcode = asm(shellcraft.sh())`, ko cần tự viết shellcode (chỉ dùng cho mấy shellcode đơn giản)

# 4. Get Flag : 

<img width="1141" height="149" alt="image" src="https://github.com/user-attachments/assets/16d55ab9-5831-4cec-9acf-01fb161fef75" />
