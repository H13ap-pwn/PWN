# 1. Find Bug :

<img width="2082" height="1217" alt="image" src="https://github.com/user-attachments/assets/73dcfad0-81ec-4381-a7b4-f11fa0210944" />

- Nhìn `struct` character & monster ta thấy `monster skill` cùng offset với 8 byte cuối của `profile character` mà `profile character` có thể viết vào, `monster skill` thì sẽ kích hoạt ở hàm `slay monster`

# 2. Idea :

- Vì `character` và `monster` cùng thuộc `1 tcachebin` -> content `monster` = content `character`

- Căn chỉnh sao cho `profile character` chứa hàm win -> khi sang monster thuộc `skill monster`

# 3. Exploit : 

<img width="1020" height="529" alt="image" src="https://github.com/user-attachments/assets/560e6d7b-fbf5-4c6c-b4ee-6fab23c02670" />

- Ta thấy `skill monster` bắt đầu ở `0x48` & `profile character` bắt đầu ở `0x20` -> cần padding 40byte + `win address`

<img width="810" height="75" alt="image" src="https://github.com/user-attachments/assets/bf6b1868-65db-44ae-ae21-83eda18d1044" />
---------------------
<img width="1278" height="537" alt="image" src="https://github.com/user-attachments/assets/9313a00a-4dc6-41c4-ae4e-c1c12f6f6267" />

- Tạo slot, tạo character

<img width="399" height="85" alt="image" src="https://github.com/user-attachments/assets/33727730-0cbd-4ab6-92b7-2912ee06e249" />
-------------------------
<img width="2553" height="719" alt="image" src="https://github.com/user-attachments/assets/efa82577-0d71-4def-bafc-2e3a5980becd" />

- Xóa `character` vừa rồi và tạo `monster`

- Dữ liệu `character` được bê nguyên sang `monster` vì bypass được `is_null`, `is_null` kiểm tra nếu con trỏ NULL sẽ tạo một bộ info mới cho `monster`. Nhưng do cơ chế `safe linking` từ libc 2.32 mặc dù chunk của `character` trỏ NULL nhưng `forward pointer` fd bị mã hóa nên luôn ko phải NULL -> bypass tự nhiên

<img width="594" height="126" alt="image" src="https://github.com/user-attachments/assets/d18f3610-c276-4160-b157-cb8861f9f4b7" />

- Cuối cùng là tạo `character` mới và `slay monster` -> get shell

# 4. Get Flag :

<img width="1254" height="903" alt="image" src="https://github.com/user-attachments/assets/2b953ef9-2913-482b-b987-a4ab44130404" />

# 5. Learned :

- Từ libc 2.32 cơ chế `Safe _ Linking` làm chunk luôn ko trỏ NULL vì đã mã hóa `forward pointer` 
