# 1. Find Bug :

![](./images/1.png)

- Buffer overflow ở `read`

- leak stdout không biết của hàm nào

# 2. Idea :

![](./images/2.png)

- Thấy NX bật -> r2shellcode ko được

- ROPChain thuần ko đủ thanh ghi

- Có thể dùng one_gadget hoặc ret2libc

![](./images/3.png)

- Nhận thấy offset = 40 nghĩa là chỉ overwrite được 6byte saved RIP -> one_gadget

# 3. Exploit :

![](./images/4.png)

- Vậy là đã biết địa chỉ được leak ra của hàm nào

![](./images/5.png)


- Viết script xác định libc base

![](./images/6.png)


- Dùng one_gadget -> offset và constraints

![](./images/7.png)


- Viết payload nhảy đến one_gadget, lưu ý có check giá trị bằng 0 tại [rbp-8]

### SCRIPT :

![](./images/8.png)


# 4. Get Flag :

![](./images/9.png)

