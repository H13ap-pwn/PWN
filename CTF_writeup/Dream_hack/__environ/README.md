# 1. Find Bug :

<img width="1924" height="738" alt="image" src="https://github.com/user-attachments/assets/c8beda45-3d73-4101-8930-027c64cd1869" />

- `stdout` -> leak libc

- `printf` cuối -> in ra nội dung mà v4 trỏ tới

# 2. Idea :

<img width="744" height="374" alt="image" src="https://github.com/user-attachments/assets/8d8cd8e3-5a5f-4e0e-9bd9-af3cac75d47f" />

------------

<img width="1275" height="330" alt="image" src="https://github.com/user-attachments/assets/ed509721-bf02-463e-afb7-6779596ffbf0" />

- Debug ta thấy open mở rồi lưu `flag` được lưu vào `buf` tại address `0x00007fffffffca60` <stack>

- Vì v4 in ra nội dung mà địa chỉ trỏ tới nên để lấy flag -> v4 = `buf` address <stack> <- Cần stack_leak <- `environ` <- libc_base

- Vòng lặp `while(1)` -> Có thể leak và gửi nhiều lần

# 3. Exploit : 

- Từ stdout -> libc_leak :

<img width="710" height="134" alt="image" src="https://github.com/user-attachments/assets/f19b0672-9102-42bc-8078-18cff16e5115" />

- Offset libc_leak và libc_base :

<img width="1309" height="1593" alt="image" src="https://github.com/user-attachments/assets/537b2c38-1527-4a8c-a948-1d37daad3a2a" />

- Tìm offset giữa libc_base và `environ` :

<img width="1202" height="195" alt="image" src="https://github.com/user-attachments/assets/e96ee3c1-6331-439b-8935-809631303553" />

- Sau khi có `environ` ta leak `stack address`

<img width="717" height="306" alt="image" src="https://github.com/user-attachments/assets/97f1fae0-55bb-4a39-a0d5-29a8df7db621" />

-----------------------------------------------------------------

<img width="1103" height="630" alt="image" src="https://github.com/user-attachments/assets/f854bb05-6213-4bec-8dbc-f4b59bad5cca" />

- Tìm offset giữa stack_leak và buf_address

<img width="2559" height="1523" alt="image" src="https://github.com/user-attachments/assets/5c81f05d-171f-4cb8-b16c-8b7b577c8705" />

- Có buf _address rồi thì gửi và get flag

<img width="756" height="249" alt="image" src="https://github.com/user-attachments/assets/ec566c00-8597-4b6f-9bea-439dcec50053" />

## SCRIPT :

<img width="1092" height="1193" alt="image" src="https://github.com/user-attachments/assets/4a093a3a-2e6a-4ef5-9fe8-7b89407db311" />

# 4. Get Flag :

<img width="1816" height="299" alt="image" src="https://github.com/user-attachments/assets/abacda0d-0d7b-4f3c-94ac-b89a4ed9cc49" />

# 5. Learned :

- `environ` : địa chỉ thuộc `libc` trỏ tới `stack address`
