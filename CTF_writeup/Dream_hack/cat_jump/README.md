# 1. Find bug :

![](./images/1.png)

- `system(s)` -> Command injection

# 2. Idea :

![](./images/2.png)


- Logic chương trình : Để chèn Command injection <- Phải win game ( Thắng >36 lần) <- Nếu random1 == 0 phải chọn `l`, nếu random1 == 1 phải chọn `h` nếu ko sẽ thua game

-> Phải predict `rand()`

# 3. Exploit :

- Từ dockerfile -> leak libc 

![](./images/3.png)


- Khai báo, load thư viện của C (vì hàm rand của C khác python)

![](./images/4.png)


- Cơ chế hoạt động của hàm `rand()`: Để `rand()` random <- `srand()` phải random <- Cần `seed` 

- Tạo seed giống chương trình từ time (số giây tính từ 1970 đến hiện tại)

- Khởi chạy srand() với seed

![](./images/5.png)


---------------

![](./images/6.png)


- Viết script logic giống chương trình, để nó tự dự đoán `rand()` và tự gửi payload để win game

- Sau khi win game -> Chèn command injection nhưng LƯU Ý : Do `snprintf(s, 0x40u, "echo \"%s\" > /tmp/cat_db", v7);` nên khi gửi lệnh vào nó sẽ hiểu đấy là văn bản thuần túy chứ ko phải lệnh vì vậy phải dùng `$(...)` để thực hiện lệnh trong ngoặc 

![](./images/7.png)


- Thêm `${IFS}` thay dấu khoảng trắng do `scanf`

## SCRIPT :

![](./images/8.png)



# 4. Get Flag :

![](./images/9.png)


# 5. Learned :

- Từ dockerfile -> có thể leak libc

- Cách predict rand()

- Một số mẹo với command injection
