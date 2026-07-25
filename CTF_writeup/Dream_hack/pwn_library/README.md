# 1. Find Bug : 

<img width="2559" height="776" alt="image" src="https://github.com/user-attachments/assets/1ab00744-ced7-4f13-becb-441fb987a88c" />

- Ở hàm `return book` có `free` nhưng ko cho con trỏ về NULL -> Use-After-Free

# 2. Idea : 

<img width="846" height="523" alt="image" src="https://github.com/user-attachments/assets/7d2c1177-ff87-4434-a053-2525b7fbb219" />

- Quan sát hàm `steal book` thấy `fread` sẽ đọc nội dung từ mở và đọc nội dung file (do mình nhập) và ghi vào vùng ptr được `malloc()` mà `malloc()` bao nhiêu mình cũng do mình nhập

-> Open file chứa flag `/home/pwnlibrary/flag.txt`(đề bài cho) và đọc vào vùng `ptr` -> `Printf` content `ptr`(Bằng cách tận dụng Use-after-free)

# 3. Exploit :

- Trước hết test local ta sẽ tạo file `flag.txt` để test

<img width="1147" height="783" alt="image" src="https://github.com/user-attachments/assets/9cb1a007-a85a-4b44-9b39-904252c78e41" />
----------------------------------
<img width="780" height="168" alt="image" src="https://github.com/user-attachments/assets/796392c4-fed8-459d-acbf-289044066795" />

- Với việc hàm `borrow book` sẽ `malloc()` lần lượt 0x100, 0x200, 0x300 với từng case và `steal book` ptr `malloc(size)` (size <= 0x190) vậy thì ta sẽ chọn case 1 ở `borrow book` -> free -> `malloc(size)` = 0x100 ở `steal book` để tận dụng use-after-free rồi dùng hàm `read book` để đọc là sẽ ra flag

- Bắt đầu test :

<img width="703" height="94" alt="image" src="https://github.com/user-attachments/assets/070bf5c2-7f65-469f-ba0b-fe6d1a4e8a3e" />
------------------------------------------------
<img width="2558" height="1597" alt="image" src="https://github.com/user-attachments/assets/0234a739-009e-41ee-b1a8-55d683eb48e3" />

- Sau khi chọn `option 1 : borrow book` và chọn case 1 ta được 1 chunk xanh lá như hình

<img width="693" height="48" alt="image" src="https://github.com/user-attachments/assets/5536fc09-fbb2-4a96-be1e-545ae6ade3cb" />
------------------------------------------------
<img width="2417" height="766" alt="image" src="https://github.com/user-attachments/assets/2a31779a-49fa-4f2a-9904-ae6d54d80094" />

- Sau khi `free` đã vào `tcache bin`

<img width="656" height="111" alt="image" src="https://github.com/user-attachments/assets/96c49934-bef7-4fbb-b4fe-560f6344af1c" />
------------------------------------------------
<img width="2085" height="661" alt="image" src="https://github.com/user-attachments/assets/ad3d1c05-e54b-474b-8a09-9492249189f6" />

- Vào `stealbook` và nhập `size` = 256(0x100) rồi `malloc()`, quan sát khi xong hàm `stealbook` thấy chunk màu xanh lá đã được ghi flag từ `fread`

<img width="1967" height="1599" alt="image" src="https://github.com/user-attachments/assets/d07e49c7-b3f8-4709-82f2-8f39e4c34726" />

- Cuối cùng `read book` sẽ ra flag

- Giờ chỉ cần thay `flag.txt` thay đường dẫn đến flag thật là xong

## SCRIPT :

  <img width="1204" height="1381" alt="image" src="https://github.com/user-attachments/assets/fd57bef7-914b-4a5c-8b9f-3b724decbcdd" />

# 4. Get Flag :

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/b018dac5-4e91-421f-b250-51520ca6ff71" />
