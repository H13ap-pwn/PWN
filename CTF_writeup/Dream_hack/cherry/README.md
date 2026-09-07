# 1. Find Bug :

<img width="2559" height="803" alt="image" src="https://github.com/user-attachments/assets/8730a5f3-2731-4c6a-a6d9-9755cd5c2314" />

- 2 hàm read -> buffer overflow 

# 2. Idea :

<img width="2520" height="744" alt="image" src="https://github.com/user-attachments/assets/514a7235-94c2-4aca-8ad4-255121447b22" />

- Overwrite return address -> flag symbol

# 3. Exploit :

<img width="1349" height="232" alt="image" src="https://github.com/user-attachments/assets/0afc2e27-600e-40b0-9195-a42f38e4886a" />
-------
<img width="1982" height="426" alt="image" src="https://github.com/user-attachments/assets/2d0c4f86-0ced-4e9a-91e5-30c29495866d" />

- PIE tắt -> Ko phải leak, có thể lấy cố định địa chỉ address (binary address)

<img width="2558" height="461" alt="image" src="https://github.com/user-attachments/assets/c946fe16-379e-41df-b76d-c914825e76be" />

- Quan sát stack có thể thấy : Với 2 lần nhập hàm read tối đa cũng ko thể chạm tới saved RIP( Chỉ tràn tới 6byte của `0x00007fffffffdea8`) nhưng :

<img width="264" height="39" alt="image" src="https://github.com/user-attachments/assets/1f930fb2-cb8c-47c5-a14f-645dbac273f1" />

- Với `read lần 2` byte đọc được lấy từ v7 -> có thể overwrite v7 để có thể tràn tới saved RIP ( Nhập bừa v7 càng lớn càng tốt)

<img width="749" height="49" alt="image" src="https://github.com/user-attachments/assets/25e140ac-a505-4d7d-8f47-933acb0c852e" />
--------------------
<img width="1241" height="474" alt="image" src="https://github.com/user-attachments/assets/4b3eb4dd-4d99-47af-8a86-37ffa388756c" />

- `Chú ý` : Khi gửi `payload lần 1` cần có `cherry` để bypass `strncmp`

- Sau khi overwrite v7 = 0x39

- Tính offset từ &v5 -> saved RIP :

<img width="2509" height="652" alt="image" src="https://github.com/user-attachments/assets/382960f5-84a7-4356-a3ff-c09614ead6dd" />

- Offset = 26 ( Trừ thêm 6byte là do 6byte đầu của `buf`)

<img width="544" height="128" alt="image" src="https://github.com/user-attachments/assets/ead8f62f-b1fb-4978-988f-54252d720c0f" />

- Overwrite return address -> `flag`

## SCRIPT :

<img width="1185" height="1403" alt="image" src="https://github.com/user-attachments/assets/65e2a369-76a4-418c-bfd7-3a452a0edbe8" />

# 4. Get Flag :

<img width="2531" height="269" alt="image" src="https://github.com/user-attachments/assets/15e67019-3805-424a-a7af-eeb8d63406e6" />
