# 1. Find Bug :

![](./images/1.png)

- Buffer Overflow ở hàm read

# 2. Idea :

![](./images/2.png)


- Chương trình leak real flag address -> overwrite v6(fake flag address) thành real flag address

- Sau khi nhập input sẽ hàm write sẽ in ra màn hình nội dung tại v6 -> in ra flag thật

# 3. Exploit :

![](./images/3.png)


- Nhận real flag address

![](./images/4.png)


- Overwrite v6 ( fake flag address ) -> real flag address, đồng thời set size mprotect = 0 để ko làm ảnh hưởng flag

### SCRIPT : 

![](./images/5.png)


# 4. Get Flag :

![](./images/6.png)

