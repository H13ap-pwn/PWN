# 1. Find Bug :

![](./images/1.png)


- 2 hàm read -> buffer overflow 

# 2. Idea :

![](./images/2.png)


- Overwrite return address -> flag symbol

# 3. Exploit :
![](./images/3.png)

-------
![](./images/4.png)


- PIE tắt -> Ko phải leak, có thể lấy cố định địa chỉ address (binary address)

![](./images/5.png)

- Quan sát stack có thể thấy : Với 2 lần nhập hàm read tối đa cũng ko thể chạm tới saved RIP( Chỉ tràn tới 6byte của `0x00007fffffffdea8`) nhưng :

![](./images/6.png)


- Với `read lần 2` byte đọc được lấy từ v7 -> có thể overwrite v7 để có thể tràn tới saved RIP ( Nhập bừa v7 càng lớn càng tốt)

![](./images/7.png)

--------------------
![](./images/8.png)


- `Chú ý` : Khi gửi `payload lần 1` cần có `cherry` để bypass `strncmp`

- Sau khi overwrite v7 = 0x39

- Tính offset từ &v5 -> saved RIP :

![](./images/9.png)


- Offset = 26 ( Trừ thêm 6byte là do 6byte đầu của `buf`)

![](./images/10.png)


- Overwrite return address -> `flag`

## SCRIPT :

![](./images/11.png)


# 4. Get Flag :
![](./images/12.png)

