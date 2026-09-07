# 1. Find Bug :

<img width="933" height="393" alt="image" src="https://github.com/user-attachments/assets/78653f6c-97b7-4a53-aad2-fc814236af20" />

- BOF ở hàm `read`

# 2. Idea :

- Tận dụng `BOF` ta có thể Overwrite saved RIP -> `target address` nhưng vì có XOR nên ta cần decode 

- Lại có thêm hàm `printf` in ra nên có thể leak libc,...

- Và chắc chắn phải bypass `strtok` để thoát vòng lặp, nếu ko Overwrite saved RIP vô nghĩa

# 3. Exploit :

<img width="2557" height="734" alt="image" src="https://github.com/user-attachments/assets/09507296-96b8-438e-ba37-d1c16f8dd1aa" />

- Có thể thấy checksec gần như bật full -> Trước hết cần leak canary

- Quan sát trên stack thấy `libc_start_call_main` -> leak được libc

<img width="423" height="67" alt="image" src="https://github.com/user-attachments/assets/929adbad-74e1-40a8-add3-6c00c690222f" />

- Theo logic của XOR X[i] = X[i] ^ X[i+1] và byte cuối sẽ giữ nguyên, nên padding 2 byte liên tiếp ko được `giống nhau` nếu ko XOR sẽ tạo ra NULL byte sớm và `printf` sẽ kết thúc trước khi leak được libc, canary

- Tìm offset canary, libc rồi leak :

<img width="779" height="440" alt="image" src="https://github.com/user-attachments/assets/72e880fa-2fb7-4d92-b51c-5e08c8200476" />
------------------------------------
<img width="1246" height="1165" alt="image" src="https://github.com/user-attachments/assets/aff5735a-c014-4ab7-a8c4-143acb260fa5" />

- Vì bài ko cho sẵn libc nên ta cần tải libc từ `Dockerfile` rồi load vào script

- Hàm decode để payload cuối sau khi XOR đúng như mình muốn :

<img width="816" height="306" alt="image" src="https://github.com/user-attachments/assets/d730094c-a57c-454a-b8de-bcc28baeb54b" />

- Để bypass `strtok` và overwrite saved RIP ta cần gửi 24 byte đầu là `\0`(encode) vì khi `strtok` kiểm tra thấy sau khi XOR thấy NULL byte sẽ dừng và trà về NULL luôn -> bypass, tiếp đến là canary(encode) và saved RBP()

- Đến đây ta có 2 hướng là `one_gadget` hoặc gọi `system(/bin/sh)` từ libc :
  
  + Theo hướng 1 sau khi thử hết các offset của `one_gadget` nhận thấy vì `RBP` luôn là 1 mà `constrant` thì cần `[RBP - x]` ra địa chỉ tồn tại và có thể viết nên khá khó thỏa mãn -> qua hướng 2 

  <img width="1308" height="102" alt="image" src="https://github.com/user-attachments/assets/e9013cb1-cb86-4b82-bae5-917428e26b99" />

  + Theo hướng 2 cần gadget `pop_rdi` và tìm `/bin/sh` có sẵn chưa

  <img width="2083" height="164" alt="image" src="https://github.com/user-attachments/assets/52c2fdef-0235-4319-a0f2-811b44a4fefa" />
  -------------------------------------------------
  <img width="2338" height="104" alt="image" src="https://github.com/user-attachments/assets/2ff6d5df-ea68-4298-b7b7-ef274fb0f0ed" />

    `/bin/sh` đã có sẵn nhưng gadget `pop_rdi` tìm ở binary ko có, qua libc tìm và đã thấy 

    <img width="1330" height="42" alt="image" src="https://github.com/user-attachments/assets/c557fe68-2b7d-475f-9ecd-55d4f1eb4604" />

    Nhưng lại có vấn đề : 
    
    <img width="2048" height="1279" alt="image" src="https://github.com/user-attachments/assets/952ce181-b3ed-49c1-a9ee-10861a66aced" />

    Lại dính `ko chia hết 16` nên ta phải kiếm thêm gadget `ret` và nhét vào payload

    <img width="1109" height="350" alt="image" src="https://github.com/user-attachments/assets/806fdc21-1fb7-4f90-92b1-b376a4ac954a" />

# 4. Get Flag :

  <img width="1476" height="260" alt="image" src="https://github.com/user-attachments/assets/b630687f-43f2-46cb-a2ad-f6b263e5cbe3" />

# 5. Learned :

- Cách tìm gadget ngoài binary còn libc 

- Cách viết decode theo logic
