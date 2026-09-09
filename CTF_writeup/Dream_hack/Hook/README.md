# 1. Find Bug:

![](./images/1.png)

- 2 free(buf) -> ko thể chạy tới system("/bin/sh")

- Thấy free(buf) -> Khả năng overwrite hook

# 2. Idea :

![](./images/2.png)


- Leak stdout -> libc leak -> libc base

![](./images/3.png)


- Thấy dòng này nghĩa là **buf = *(buf+1) và buf sau cách buf trước 8byte do QWORD -> Nhập vào read 8byte của __free_hook và 8byte của system

# 3. Exploit :

![](./images/4.png)


- Đầu tiên ta sẽ tìm libc base

- Giờ chỉ cần overwrite __free_hook = system("/bin/sh") nhưng ko thể set tham số /bin/sh nên ta sẽ nhảy tới chỗ set /bin/sh để nó chạy tiếp đến system, chứ ko nhảy thẳng đến system

![](./images/5.png)


### SCRIPT :

![](./images/6.png)


# 4. Get Flag :

![](./images/7.png)

