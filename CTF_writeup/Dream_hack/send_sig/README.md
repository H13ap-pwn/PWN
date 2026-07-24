# 1. Find Bug :

<img width="2543" height="912" alt="image" src="https://github.com/user-attachments/assets/d94dbc7b-477c-4fd0-856a-39baa04c3e73" />

----------------------

<img width="806" height="254" alt="image" src="https://github.com/user-attachments/assets/f92f00a6-5387-4ca0-aa45-ae73be188bcb" />

- File bị `stripped`

- Buffer overflow ở hàm `read`

# 2. Idea :

<img width="1545" height="263" alt="image" src="https://github.com/user-attachments/assets/ff7d3688-c4af-4bcb-9a92-1536894c5dfc" />

- Ko thể leak libc

- ko có hàm nào chạy `system`, `execve`

- Ko đủ gadget để ROPgadget thuần

- NX bật -> ko ret2shellcode

-> Mà tràn rất nhiều byte, có thể dùng SROP

# 3. Exploit :

- Offset từ `buf` đến saved RIP là `16`(8 byte cho `buf`, 8byte cho `saved RBP`)

<img width="2418" height="644" alt="image" src="https://github.com/user-attachments/assets/b0100afe-9352-468c-834d-c64e84eacf54" />

- Lấy được 2gadget `pop rax` và `syscall`

<img width="2075" height="376" alt="image" src="https://github.com/user-attachments/assets/2cbbd73c-99b8-4c08-8abb-a5102c427581" />

- Có sẵn `/bin/sh`

## SCRIPT SROP chạy execve :

<img width="596" height="513" alt="image" src="https://github.com/user-attachments/assets/ab8221e9-e7a8-47fa-8a7b-e27f5ee9af11" />

# 4. Get Flag :

<img width="1814" height="306" alt="image" src="https://github.com/user-attachments/assets/c0d23563-137a-45b1-8430-a7da11a11a0c" />
