# 1. Find Bug :

<img width="2544" height="889" alt="image" src="https://github.com/user-attachments/assets/9f219ff7-1a87-40b9-8308-2a5c30327f6b" />

- `i = buf[i]` <- `buf[i] = value` <- `value` do mình nhập mà `value` lại ở dạng int64 nên có thể nhập âm mặc dù `scanf` ở dạng `%lu` (có thể tự chuyển số âm nhập vào thành dạng unsigned)

-> Có thể truy cập `i` < 0 -> OUT OF BOUND

- Có hàm `win`

# 2. Idea :

<img width="1454" height="282" alt="image" src="https://github.com/user-attachments/assets/25b5a836-2d25-4ca7-9e35-5a804b54a409" />

- PIE tắt -> ko phải leak binary address

<img width="1472" height="57" alt="image" src="https://github.com/user-attachments/assets/dd8060bf-dac4-4da2-a381-06397233583d" />

----------------

<img width="1339" height="213" alt="image" src="https://github.com/user-attachments/assets/a0a95644-91c5-4f68-b71b-56dfb6b5dd3b" />

- Có thể thấy `buf` ở `0x404080` còn `GOTprintf` ở `0x404008` cách nhau `120` -> `buf[-15]` sẽ là `GOTprintf`  -> Overwrite GOT -> `win`

# 3. Exploit :

<img width="699" height="160" alt="image" src="https://github.com/user-attachments/assets/f7b0dcd3-555e-466e-859d-c71daf20e32d" />

- `Payload 1` để set `i = -15`

<img width="1361" height="119" alt="image" src="https://github.com/user-attachments/assets/e81544a4-89e4-44a5-8e70-3b0eb67d4537" />

- `Payload 2` để Overwrite `GOTprintf` -> win

# 4. Get Flag :

<img width="1754" height="257" alt="image" src="https://github.com/user-attachments/assets/66d481c1-434f-4801-8e36-d7ccc7de4e18" />
