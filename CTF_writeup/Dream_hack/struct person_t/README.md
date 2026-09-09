# 1. Find Bug :

![](./images/1.png)

- Buffer overflow ở hàm `sub_40123A(nation, 128)` do trong đó có hàm `read` với 2 tham số truyền vào :

![](./images/2.png)


- Và ở bên trái ta thấy có hàm `sub_401216` chạy `execve`

![](./images/3.png)

# 2. Idea :

- Tìm cách leak & bypass `canary`

- Overwrite saved RIP -> `sub_401216`

# 3. Exploit :

![](./images/4.png)


- Trước hết ta thấy file bị stripped

- PIE tắt -> Có thể hardcore thẳng địa chỉ hàm `sub_401216`

![](./images/5.png)

- Ở hàm `sub_40123A` : Nếu kí tự cuối là `\n` -> `\0` -> Nếu ta nhập full size sẽ ko dính `\0`

-> Để leak canary ta nhập full size `name`, nhập số thật lớn cho `age` và `height` để ko dính NULL byte, và quan trọng nhất là 5 byte ở `&age + 4` để nối thẳng tới `canary` 

![](./images/6.png)


-------------------------------

![](./images/7.png)


- Sau `DEBUG` ta thấy canary đã chuẩn giờ tiếp theo là overwrite saved RIP -> `sub_401216`

![](./images/8.png)


- Vào `ida` ta có thể thấy nó ở địa chỉ `0x0000000000401216`

- `canary` có, `địa chỉ cần overwrite` có -> tính offset từ `nation` đến `saved RIP` là xong

![](./images/9.png)


## SCRIPT :

![](./images/10.png)


# 4. Get Flag :

![](./images/11.png)

