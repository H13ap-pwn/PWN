# 1. Find Bug :

<img width="2557" height="1268" alt="image" src="https://github.com/user-attachments/assets/f6115f11-ea79-480a-bfff-759bf0e567d4" />

- Nhập shellcode vào vùng được `mmap`

# 2. Idea :

<img width="648" height="172" alt="image" src="https://github.com/user-attachments/assets/fd990108-84b7-4401-97b6-e05c24d76475" />

- Vì `dup2` điều hướng shell vào `/dev/null` -> Reverse shell

# 3. Exploit :

## SCRIPT :

<img width="1182" height="1383" alt="image" src="https://github.com/user-attachments/assets/be452895-5cd2-4dca-be14-80b7fff19389" />

- Reverse shell : 
  + Với local : Ta kết nối với `localhost`, port 12345 rồi dùng `dup2` + `socket` + `connect` để điều hướng stdin(0), stdout(1), stderr(2) để terminal đang listen port có thể nhập input, output
thì lúc này `socket_address` sẽ là `.quad 0x100007F39300002` ( IP + port + IPv4 )
  + Với sever : Vẫn mở terminal nghe ở port 12345 nhưng `socket_address` sẽ là `.quad 0xF9658A12C5490002`, đây là IP + port của `ngrok`(kết nối thẳng sever đến localhost)

# 4. Get Flag : 

<img width="2551" height="1584" alt="image" src="https://github.com/user-attachments/assets/484579d7-8e32-4add-a3bb-a45c27d7b776" />

# 5. Learned :

- Reverse shell : Giúp điều hướng stdin, stdout, stderr về terminal của mình
