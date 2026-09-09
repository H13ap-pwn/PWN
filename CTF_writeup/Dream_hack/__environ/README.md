# 1. Find Bug :

![](./images/1.png)

- `stdout` -> leak libc

- `printf` cuối -> in ra nội dung mà v4 trỏ tới

# 2. Idea :

![](./images/2.png)


------------

![](./images/3.png)


- Debug ta thấy open mở rồi lưu `flag` được lưu vào `buf` tại address `0x00007fffffffca60` <stack>

- Vì v4 in ra nội dung mà địa chỉ trỏ tới nên để lấy flag -> v4 = `buf` address <stack> <- Cần stack_leak <- `environ` <- libc_base

- Vòng lặp `while(1)` -> Có thể leak và gửi nhiều lần

# 3. Exploit : 

- Từ stdout -> libc_leak :

![](./images/4.png)


- Offset libc_leak và libc_base :

![](./images/5.png)


- Tìm offset giữa libc_base và `environ` :

![](./images/6.png)


- Sau khi có `environ` ta leak `stack address`

![](./images/7.png)


-----------------------------------------------------------------

![](./images/8.png)


- Tìm offset giữa stack_leak và buf_address

![](./images/9.png)


- Có buf _address rồi thì gửi và get flag

![](./images/10.png)


## SCRIPT :

![](./images/11.png)


# 4. Get Flag :

![](./images/12.png)


# 5. Learned :

- `environ` : địa chỉ thuộc `libc` trỏ tới `stack address`
