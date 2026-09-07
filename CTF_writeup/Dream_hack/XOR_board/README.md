# 1. Find Bug :

<img width="967" height="408" alt="image" src="https://github.com/user-attachments/assets/5167143b-13da-4f4a-b0d5-5d433b0580c6" />

- i, j là các index của mảng như kiểu dữ liệu `int` -> OOB

# 2. Idea :

<img width="1486" height="1405" alt="image" src="https://github.com/user-attachments/assets/f109e6d1-6a44-45e9-bd73-6c37517022f6" />
---------------------------------
<img width="1360" height="203" alt="image" src="https://github.com/user-attachments/assets/173423d7-360a-4e7d-8a63-87e8701a87ef" />

- Xem index quanh `arr` thấy có các GOT đồng thời Relro tắt + tận dụng `xor` -> Overwrite GOT

# 3. Exploit :

- Lựa chọn `GOT scanf`, có 2 hướng
  + Hướng 1 : XOR `GOT scanf` với chính nó cho về 0 -> xor tiếp với `win`. Nhưng cách này ko được vì khi XOR `GOT scanf` về 0 thì ngay sau đó lại gọi `scanf` trước khi nó chạy hàm `win` -> fail 
  + Hướng 2 : XOR `GOT scanf` với 1 số trung gian ( tạm gọi là mask ) -> `win` ( Dùng được )

- STAGE 1 : LEAK binary base -> win ( do PIE bật )

  <img width="1515" height="444" alt="image" src="https://github.com/user-attachments/assets/85dda23b-2fe2-4469-861f-f6eb17f2c4fb" />
  
  + Tại index = -7 ta tìm được 1 địa chỉ binary nhưng do hàm `print` ko in được tại index âm -> Ta cần xor 1 index dương nào đó hiện tại giá trị bằng 0 ( chọn 100 ) với index -7 rồi in ra

  + Sau khi có binary leak -> binary base -> `win`

  <img width="743" height="523" alt="image" src="https://github.com/user-attachments/assets/f4898d3f-ee54-4923-8e54-cd8d424326e3" />
  ---------------------------------------
  <img width="1193" height="967" alt="image" src="https://github.com/user-attachments/assets/d2d814c3-4980-49ba-82b6-beffd2f6a445" />

- STAGE 2 : LEAK GOT scanf 
  
  <img width="1434" height="461" alt="image" src="https://github.com/user-attachments/assets/26a44dff-c2aa-4aa9-b204-9c715265ac70" />

  + `GOT scanf` cũng ở index âm -> leak tương tự STAGE 1

  <img width="723" height="368" alt="image" src="https://github.com/user-attachments/assets/bbbf5c71-b7d4-4cb0-a054-f9ea4c8755d6" />
  -------------------------------------------
  <img width="995" height="974" alt="image" src="https://github.com/user-attachments/assets/828ef444-49ce-4a72-b17e-e771fbd2f943" />

- STAGE 3 : Tìm mask 
  + Ta có `GOT scanf` XOR `mask` = `win` -> `mask` = `GOT scanf` XOR `win` ( Tính chất của `XOR` )

  + Tạo mask ở index trung gian khác ( chọn 102 ) để khi xong chỉ cần XOR `GOT scanf` một lần là get shell ( tránh XOR `GOT scanf` nhiều lần bị lỗi)

  <img width="700" height="87" alt="image" src="https://github.com/user-attachments/assets/181890a7-0410-47ee-8796-89d85b02b223" />
  ----------------------
  <img width="1349" height="41" alt="image" src="https://github.com/user-attachments/assets/4f0de5d6-73f8-412c-a0c3-0d99d9bd7176" />

  + Chuyển mask -> số nhị phân 

  <img width="1071" height="906" alt="image" src="https://github.com/user-attachments/assets/d28bac25-652b-47a7-9c81-6655252d6ab6" />

  + Và điều đặc biệt ở `arr` đó là giá trị(nhị phân) tại các index 0,1,3,4 ,... lần lượt là 0..1, 0..10, 0..100, 0..1000 -> Tận dụng điều đó ta sẽ tạo được mask

  <img width="770" height="297" alt="image" src="https://github.com/user-attachments/assets/27f7b30d-d019-4be8-ba91-5750d2df667d" />

  + Với 64bit nên ta sẽ quét các bit của `mask` 63 lần với index i từ 0 -> 63

  + Và sau mỗi `i` vòng lặp ta sẽ dịch phải mask `i` bit và `&1` để xét bit cuối cùng ( Xét lần lượt từng bit của mask ) 

  + Nếu bit của `mask` là 1 thì sẽ XOR index trung gian với đúng index `i`

- STAGE 4 : `GOT scanf` XOR `mask`

    <img width="706" height="158" alt="image" src="https://github.com/user-attachments/assets/18b9f393-6e87-4e98-aa3e-78b065ad3387" />

# 4. Get Flag :

<img width="1594" height="564" alt="image" src="https://github.com/user-attachments/assets/2d75a5f9-f5be-41dc-8d55-34128dd83c91" />

