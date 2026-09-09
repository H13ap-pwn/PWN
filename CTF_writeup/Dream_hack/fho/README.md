# 1. Find Bug :

![](./images/1.png)

- BOF ở hàm `read`

- `free(ptr)` -> tận dụng __free_hook

# 2. Idea :

![](./images/2.png)


- `*ptr = v5` và được nhập cả 2 -> Overwrite `__free_hook` thành `target address`

# 3. Exploit :

- STAGE 1 : LEAK LIBC

  ![](./images/3.png)


  + Leak `libc start main` với padding đã tính toán là `72` nhờ BOF và hàm `printf("Buf: %s\n", buf)`

  ![](./images/4.png)

  ---------------------------------
  ![](./images/5.png)


  + Sau khi có libc_leak -> libc_base

- STAGE 2 : Overwrite GOT

  + Với việc có libc_base -> Dùng `one_gadget`

  ![](./images/6.png)


  + `target address` = `libc_base` + `offset` ( Thử lần lượt các offset ở one_gadget)

  ![](./images/7.png)


# 4. Get Flag :

![](./images/8.png)

