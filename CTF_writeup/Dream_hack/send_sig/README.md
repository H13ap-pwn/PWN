# 1. Find Bug :

![](./images/1.png)

----------------------

![](./images/2.png)

- File bị `stripped`

- Buffer overflow ở hàm `read`

# 2. Idea :

![](./images/3.png)


- Ko thể leak libc

- ko có hàm nào chạy `system`, `execve`

- Ko đủ gadget để ROPgadget thuần

- NX bật -> ko ret2shellcode

-> Mà tràn rất nhiều byte, có thể dùng SROP

# 3. Exploit :

- Offset từ `buf` đến saved RIP là `16`(8 byte cho `buf`, 8byte cho `saved RBP`)

![](./images/4.png)


- Lấy được 2gadget `pop rax` và `syscall`

![](./images/5.png)


- Có sẵn `/bin/sh`

## SCRIPT SROP chạy execve :

![](./images/6.png)


# 4. Get Flag :

![](./images/7.png)

