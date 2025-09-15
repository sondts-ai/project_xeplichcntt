# 📅 Xếp lịch Khoa CNTT - ĐH Kiến trúc  

Ứng dụng **Streamlit** hỗ trợ **xếp lịch học tự động** cho Khoa CNTT bằng **thuật toán Hill Climbing + Random Restart**.  
Người dùng chỉ cần nhập thông tin **lớp, môn học, giảng viên, số buổi** → hệ thống sẽ tự động sinh ra **lịch học tối ưu**.  

---

## 🚀 Tính năng  

- Nhập dữ liệu các buổi học: **lớp, môn học, giảng viên, số buổi**.  
- Kiểm tra ràng buộc:  
  - Giảng viên không vượt quá **24 buổi/tuần**.  
  - Không trùng **phòng / giảng viên / lớp** trong cùng một slot.  
- Sinh lịch tự động bằng **Random Restart Hill Climbing**.  
- Hiển thị lịch học dạng **bảng (tuần / ca)**.  
- Đánh giá lịch theo tiêu chí: **phân bố đều, tránh dồn ca**.  

---

## 📂 Cấu trúc dự án  

```
project/
│── sche.py          # Các hàm xử lý sinh lịch, evaluate, neighbor, hill climbing
│── app.py           # Giao diện Streamlit
│── requirements.txt # Thư viện cần cài
│── README.md        # Tài liệu dự án
```

---

## ⚙️ Cài đặt  

1. Clone project  
```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
```

2. Tạo môi trường ảo (khuyến nghị)  
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Cài thư viện  
```bash
pip install -r requirements.txt
```

---

## ▶️ Chạy ứng dụng  

```bash
streamlit run app.py
```

Ứng dụng sẽ mở trên trình duyệt tại: **http://localhost:8501**  

---

## 📊 Demo  

1. Nhập dữ liệu buổi học.  
2. Nhấn nút **"🔄 Sinh lịch khoa CNTT"**.  
3. Xem lịch học được sinh tự động dưới dạng bảng.  

---

## 🛠️ Công nghệ sử dụng  

- **Python 3.10+**  
- **Streamlit** – xây dựng giao diện web nhanh chóng  
- **Pandas** – xử lý dữ liệu & hiển thị bảng  