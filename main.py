print (" --- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN --- ")

name_patient = input ("Nhập tên bệnh nhân : ")

# Ép kiểu dữ liệu sang float
weight = float(input ("Nhập cân nặng bệnh nhân : "))

print (" --- KIỂM TRA DỮ LIỆU LƯU TRỮ --- ")

print ("Bệnh nhân : ", name_patient)
print ("Cân nặng đã nhập : ", weight)

# Kiểm tra kiểu dữ liệu
print ("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))


'''
# (1) Phân tích lỗi

## a. Dò luồng thực thi của chương trình (trace code)

Khi chương trình bắt đầu chạy, hệ thống yêu cầu điều dưỡng viên nhập cân nặng của bệnh nhân thông qua hàm `input()`. Ví dụ, người dùng nhập giá trị `65.5`. Dữ liệu này sau đó được lưu vào biến của chương trình để tiếp tục xử lý và kiểm tra kiểu dữ liệu trước khi lưu vào cơ sở dữ liệu.

Tuy nhiên, mặc dù người dùng nhập vào một giá trị có dạng số thực, Python vẫn lưu dữ liệu đó dưới dạng chuỗi ký tự. Điều này xảy ra vì hàm `input()` trong Python mặc định luôn trả về kiểu dữ liệu `str`. Do đó, giá trị `"65.5"` mà hệ thống nhận được thực chất chỉ là một chuỗi văn bản chứ chưa phải số thực.

Khi hệ thống kiểm tra kiểu dữ liệu bằng hàm `type()`, kết quả hiển thị là:

```python id="iv6zfc"
<class 'str'>
```

Điều này cho thấy dữ liệu đang được lưu dưới dạng chuỗi thay vì kiểu `float` như yêu cầu của hệ thống quản lý y khoa.

---

## b. Giải thích đặc điểm của hàm `input()` trong Python

Trong Python, hàm `input()` được sử dụng để nhận dữ liệu từ bàn phím người dùng. Tuy nhiên, đặc điểm quan trọng của hàm này là mọi dữ liệu nhập vào đều được Python tự động chuyển thành kiểu chuỗi (`str`), bất kể người dùng nhập chữ hay số.

Ví dụ:

```python id="f9tt2m"
weight = input("Nhập cân nặng: ")
```

Nếu người dùng nhập:

```text id="4smw1v"
65.5
```

thì Python sẽ hiểu dữ liệu là:

```python id="r2ltu9"
"65.5"
```

chứ không phải số thực `65.5`.

Điều này giúp Python linh hoạt trong việc tiếp nhận dữ liệu nhập từ người dùng, nhưng lập trình viên cần chủ động ép kiểu dữ liệu nếu muốn thực hiện các phép tính toán học.

---

## c. Nguyên nhân dữ liệu nhập là số nhưng lại được lưu dưới dạng chuỗi

Nguyên nhân chính là do chương trình chưa thực hiện ép kiểu dữ liệu từ `str` sang `float` sau khi nhận dữ liệu bằng hàm `input()`.

Mặc dù điều dưỡng viên nhập vào giá trị có dạng số thực, nhưng Python vẫn xem đó là chuỗi ký tự vì hàm `input()` mặc định trả về kiểu `str`. Do hệ thống không sử dụng hàm `float()` để chuyển đổi dữ liệu nên giá trị cân nặng vẫn bị lưu sai kiểu dữ liệu.

Ví dụ:

```python id="sv6q6m"
weight = input("Nhập cân nặng: ")
```

Sau câu lệnh trên:

```python id="u2wycu"
weight = "65.5"
```

và kiểu dữ liệu là:

```python id="h9dn9d"
<class 'str'>
```

Chính vì vậy, hệ thống không thể thực hiện các phép tính như tính BMI, bởi máy tính không thể tính toán trực tiếp với dữ liệu dạng chuỗi ký tự.



'''