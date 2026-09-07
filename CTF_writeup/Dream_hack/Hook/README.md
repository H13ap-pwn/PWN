# 1. Find Bug:

<img width="2108" height="674" alt="image" src="https://github.com/user-attachments/assets/7314ce41-375a-40eb-bdca-e26505ed868a" />

- 2 free(buf) -> ko thể chạy tới system("/bin/sh")

- Thấy free(buf) -> Khả năng overwrite hook

# 2. Idea :

<img width="564" height="39" alt="image" src="https://github.com/user-attachments/assets/7038cd85-f91c-4874-bc00-e16b9b1dc51b" />

- Leak stdout -> libc leak -> libc base

<img width="712" height="39" alt="image" src="https://github.com/user-attachments/assets/5366e535-0993-4e23-b5a5-94af8b090868" />

- Thấy dòng này nghĩa là **buf = *(buf+1) và buf sau cách buf trước 8byte do QWORD -> Nhập vào read 8byte của __free_hook và 8byte của system

# 3. Exploit :

<img width="754" height="195" alt="image" src="https://github.com/user-attachments/assets/25ae7662-3d8e-47ee-8020-2ab979e5dac2" />

- Đầu tiên ta sẽ tìm libc base

- Giờ chỉ cần overwrite __free_hook = system("/bin/sh") nhưng ko thể set tham số /bin/sh nên ta sẽ nhảy tới chỗ set /bin/sh để nó chạy tiếp đến system, chứ ko nhảy thẳng đến system

<img width="1227" height="80" alt="image" src="https://github.com/user-attachments/assets/bf85c819-fd32-4d88-980a-f1d96aa09924" />

### SCRIPT :

<img width="1008" height="1370" alt="image" src="https://github.com/user-attachments/assets/c4259333-8320-4ed7-b022-aa7c97384a36" />

# 4. Get Flag :

<img width="1474" height="98" alt="image" src="https://github.com/user-attachments/assets/ecdb7c6a-82b8-4be3-8201-14c1135c9eb6" />
