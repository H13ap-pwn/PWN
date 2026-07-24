# 1. Find bug :

<img width="811" height="204" alt="image" src="https://github.com/user-attachments/assets/54700a28-46b1-4f0d-a65d-5cc9b909f1f1" />

- `system(s)` -> Command injection

# 2. Idea :

<img width="1881" height="1456" alt="image" src="https://github.com/user-attachments/assets/291f4e4e-92c1-48b0-8dc3-02a9ab69ad49" />

- Logic chương trình : Để chèn Command injection <- Phải win game ( Thắng >36 lần) <- Nếu random1 == 0 phải chọn `l`, nếu random1 == 1 phải chọn `h` nếu ko sẽ thua game

-> Phải predict `rand()`

# 3. Exploit :

- Từ dockerfile -> leak libc 

<img width="997" height="209" alt="image" src="https://github.com/user-attachments/assets/ff3b95ff-6371-495d-9718-39a21d31f85b" />

- Khai báo, load thư viện của C (vì hàm rand của C khác python)

<img width="446" height="67" alt="image" src="https://github.com/user-attachments/assets/4532ac56-428d-4691-97ee-9acf06284000" />

- Cơ chế hoạt động của hàm `rand()`: Để `rand()` random <- `srand()` phải random <- Cần `seed` 

- Tạo seed giống chương trình từ time (số giây tính từ 1970 đến hiện tại)

- Khởi chạy srand() với seed

<img width="1064" height="671" alt="image" src="https://github.com/user-attachments/assets/7ad79e8a-6056-4945-aef0-636f90b6f5ac" />

---------------

<img width="2559" height="1558" alt="image" src="https://github.com/user-attachments/assets/9518c450-828f-43b8-91d0-04b328877dce" />

- Viết script logic giống chương trình, để nó tự dự đoán `rand()` và tự gửi payload để win game

- Sau khi win game -> Chèn command injection nhưng LƯU Ý : Do `snprintf(s, 0x40u, "echo \"%s\" > /tmp/cat_db", v7);` nên khi gửi lệnh vào nó sẽ hiểu đấy là văn bản thuần túy chứ ko phải lệnh vì vậy phải dùng `$(...)` để thực hiện lệnh trong ngoặc 

<img width="563" height="81" alt="image" src="https://github.com/user-attachments/assets/14d3a065-57b1-4339-8817-cb2431096d80" />

- Thêm `${IFS}` thay dấu khoảng trắng do `scanf`

## SCRIPT :

<img width="1673" height="1370" alt="image" src="https://github.com/user-attachments/assets/10e55ec4-7ac4-4650-8f23-ccb1a0d2fb21" />


# 4. Get Flag :

<img width="1690" height="391" alt="image" src="https://github.com/user-attachments/assets/40ac90ce-37dd-400d-bdd1-00db9bb3c891" />

# 5. Learned :

- Từ dockerfile -> có thể leak libc

- Cách predict rand()

- Một số mẹo với command injection
