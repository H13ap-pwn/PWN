# 1. Find bug :
<img width="1171" height="370" alt="image" src="https://github.com/user-attachments/assets/7f94a3a7-d8b0-4383-939a-6d9730f19470" />

- Viết shell code

# 2. Idea :

- Viết shellcode

<img width="1500" height="268" alt="image" src="https://github.com/user-attachments/assets/0b60089c-c746-4440-b215-c06d121be619" />

- Mặc dù NX bật nhưng do mmap như vùng nhớ khác heap, stack, ... nên vẫn viết shellcode được

- Nhận thấy banned_execve nên sẽ dùng shellcode open,read,write

# 3. Exploit:
<img width="1048" height="1341" alt="image" src="https://github.com/user-attachments/assets/f29674e0-3af1-4ff4-a968-e52e4e044941" />

# 4. Get Flag:
<img width="1655" height="483" alt="image" src="https://github.com/user-attachments/assets/c8624cd8-74c7-45dc-9083-f260a95798f9" />
