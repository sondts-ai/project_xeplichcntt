# 📅 Xếp lịch Khoa CNTT - ĐH Kiến trúc

Ứng dụng Streamlit hỗ trợ **xếp lịch học tự động** cho khoa CNTT bằng thuật toán **Hill Climbing + Random Restart**.  
Người dùng chỉ cần nhập thông tin lớp, môn học, giảng viên và số buổi → hệ thống sẽ tự sinh ra lịch học tối ưu.

---

## 🚀 Tính năng
- Nhập dữ liệu các buổi học: lớp, môn, giảng viên, số buổi.
- Kiểm tra ràng buộc:
  - Giảng viên không vượt quá 24 buổi/tuần.
  - Không trùng phòng, giảng viên, lớp tại cùng một slot.
- Sinh lịch tự động bằng **Random Restart Hill Climbing**.
- Hiển thị lịch học dạng bảng (tuần / ca).
- Đánh giá lịch dựa trên tiêu chí phân bố đều, tránh dồn ca.

---

## 📂 Cấu trúc dự án
project/
│── sche.py # Các hàm xử lý sinh lịch, đánh giá, neighbor, hill climbing
│── app.py # Giao diện Streamlit
│── requirements.txt # Thư viện cần cài
│── README.md # Tài liệu dự án




---

## ⚙️ Cài đặt

### 1. Clone project
```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

2. Tạo môi trường ảo (khuyến nghị)
bash
Copy code
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Cài thư viện
bash
Copy code
pip install -r requirements.txt
▶️ Chạy ứng dụng
bash
Copy code
streamlit run app.py
Ứng dụng sẽ mở trên trình duyệt tại http://localhost:8501.

📊 Demo
Nhập dữ liệu buổi học.

Nhấn "🔄 Sinh lịch khoa CNTT".

Xem lịch học được sinh tự động dạng bảng.

🛠️ Công nghệ sử dụng
Python 3.10+

Streamlit – xây dựng giao diện web nhanh chóng.

Pandas – xử lý dữ liệu, hiển thị bảng.