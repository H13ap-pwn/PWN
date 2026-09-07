# 1. Find Bug :

<img width="2447" height="1017" alt="image" src="https://github.com/user-attachments/assets/df4ef805-ea4e-4e67-8041-57a297375dd3" />

- Buffer Overflow ở hàm read

# 2. Idea :

<img width="1400" height="183" alt="image" src="https://github.com/user-attachments/assets/8eed511b-185d-490d-89fe-089c0c128b7c" />

- Chương trình leak real flag address -> overwrite v6(fake flag address) thành real flag address

- Sau khi nhập input sẽ hàm write sẽ in ra màn hình nội dung tại v6 -> in ra flag thật

# 3. Exploit :

<img width="806" height="116" alt="image" src="https://github.com/user-attachments/assets/95a8f780-6f5d-44eb-9501-82d6d5747e01" />

- Nhận real flag address

<img width="570" height="194" alt="image" src="https://github.com/user-attachments/assets/6d869258-f1b6-44d9-a22c-6849f2c10766" />

- Overwrite v6 ( fake flag address ) -> real flag address, đồng thời set size mprotect = 0 để ko làm ảnh hưởng flag

### SCRIPT : 

<img width="1038" height="1390" alt="image" src="https://github.com/user-attachments/assets/45a598d2-a05d-4c04-b673-82c08a80e5f6" />

# 4. Get Flag :

<img width="1973" height="974" alt="image" src="https://github.com/user-attachments/assets/b3fadf6e-3641-452b-b4ff-fe0ea2628641" />
