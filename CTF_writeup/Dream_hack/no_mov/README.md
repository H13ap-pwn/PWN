# 1. Find Bug :

<img width="2550" height="887" alt="image" src="https://github.com/user-attachments/assets/7612d25a-ad5a-440f-bdea-def9d23d9c0c" />

- Viết shellcode

# 2. Idea :

<img width="1057" height="814" alt="image" src="https://github.com/user-attachments/assets/e00cfcef-0757-4c6c-bf65-76388910d503" />

- Vào verify là check các byte của shellcode, nếu trùng -> ko thực thi được ( Phải viết shellcode né các byte bị chặn )

# 3. Exploit :

<img width="851" height="476" alt="image" src="https://github.com/user-attachments/assets/899ab3d3-70a9-4ca3-9d78-ad867318ddd1" />

- `p64()` lần lượt vào để xem những `byte bị chặn`

- Viết 1 đoạn shellcode basic -> chuyển lần lượt các lệnh thành raw bytes -> lệnh nào trùng `byte bị chặn` -> fix, ví dụ :

<img width="594" height="353" alt="image" src="https://github.com/user-attachments/assets/384fa8eb-3354-4fea-a6b4-ce2a99d5ab7b" />

-------------------

<img width="754" height="71" alt="image" src="https://github.com/user-attachments/assets/336390cc-b658-4e7f-9d36-51c63a532e77" />

- Như lệnh này gán 1 số cho 1 thanh ghi -> ko được do dính byte bị chặn `c7`

- Từ shellcode basic, check từng dòng lệnh -> fix lần lượt ta được shellcode hoàn chỉnh bypass `verify` :

<img width="710" height="887" alt="image" src="https://github.com/user-attachments/assets/e083857f-f79c-488f-beb4-2af3aaee18e7" />

- `LƯU Ý` : Nếu `push` thẳng 1 số thì chỉ được `4byte` nên phải push 2 lần `/bin//sh`

## SCRIPT :

<img width="1129" height="1411" alt="image" src="https://github.com/user-attachments/assets/f5e3042c-7a33-44ba-b818-18a2c884b686" />

# 4. Get Flag :

<img width="1490" height="260" alt="image" src="https://github.com/user-attachments/assets/6e51198e-5280-4749-b31f-dd997b69d4f7" />

# 5. Learned :

- Cách chuyển code shellcode -> byte 
