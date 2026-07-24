# 1. Find Bug :

<img width="2547" height="1041" alt="image" src="https://github.com/user-attachments/assets/40be68ec-548d-4c16-9838-bcc997326b3e" />

- Tổng quan là sẽ có 4 option -> đi sâu vào từng option

<img width="1016" height="75" alt="image" src="https://github.com/user-attachments/assets/036ef0ab-aa24-4314-ad01-d4c8a8e4aad5" />

- Với hàm `write_file` thì nhập vào `write_buffer` và mở file `test` lấy dữ liệu từ `write_buffer` -> buffer overflow

<img width="1132" height="284" alt="image" src="https://github.com/user-attachments/assets/1d2bbd74-f1c4-407c-b344-7c8444f85212" />

- Với `show_contents` thì in ra màn hình, lấy dữ liệu từ `read_buffer`

<img width="979" height="47" alt="image" src="https://github.com/user-attachments/assets/55cf1731-baa4-49aa-b852-385d9d33c5ea" />

- Với hàm `flag` thì ghi nội dung flag vào `flag`

<img width="914" height="51" alt="image" src="https://github.com/user-attachments/assets/5bec4b5a-622d-41f5-a70e-f28f12bf06dd" />

- `read file` đọc nội dung file `test` vào `readbuffer`

# 2. Idea :

- Chọn option 2 `write_file` nhập tràn -> ghi vào file `text` số lượng tối đa là 64byte

- Chọn option 1 gồm cả `read_flag` và `read file` -> `read file` sẽ ghi 64byte nội dung từ file `text` vào `readbuffer` -> sẽ nối chuỗi với `flag` luôn do ko có byte NULL

- Chọn option 3 `show_contents` in ra màn hình nội dung của `readbuffer` -> in ra flag

# 3. Exploit :

<img width="1965" height="960" alt="image" src="https://github.com/user-attachments/assets/fccf68fc-230e-4a34-832b-c64d82e42408" />

- Vậy khi nhập `write_file` ta nhập >= 64 cũng được vì khi ghi vào file text cũng chỉ tối đa 64byte và từ 64byte ấy sẽ được `readbuffer` nối chuỗi với flag

 <img width="518" height="84" alt="image" src="https://github.com/user-attachments/assets/8f1c7a18-0432-411f-aa8e-73b0dd058ad8" />

- Sau đó chọn option 1 để `read_file` ghi nội dung file text vào `readbuffer` để nối với flag rồi chọn option3 `show_contents` là in ra flag

<img width="453" height="72" alt="image" src="https://github.com/user-attachments/assets/ef27cf70-fe37-4891-967c-de35e2672d72" />

### SCRIPT :

<img width="1175" height="1345" alt="image" src="https://github.com/user-attachments/assets/f333a18c-7155-45c5-9501-3f483ffb5e05" />

# 4. Get Flag :

<img width="2320" height="427" alt="image" src="https://github.com/user-attachments/assets/f986e69f-be1c-49db-b1d5-cd3341485146" />
