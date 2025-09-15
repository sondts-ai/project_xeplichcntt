import streamlit as st
import pandas as pd
from sche import random_restart_hill_climbing, evaluate, days, cas

st.title("📅 Xếp lịch Khoa CNTT - ĐH Kiến trúc")

if "sessions" not in st.session_state:
    st.session_state.sessions = []

col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
with col1:
    cls = st.text_input("Tên lớp")
with col2:
    subj = st.text_input("Môn học")
with col3:
    teacher = st.text_input("Giảng viên")
with col4:
    count = st.number_input("Số buổi", min_value=1, max_value=30, value=1, step=1)

if st.button("➕ Thêm buổi học"):
    teacher_count = sum(s[3] for s in st.session_state.sessions if s[2] == teacher) + count
    if teacher_count > 24:
        st.warning(f"⚠️ Giảng viên {teacher} vượt quá 24 buổi/tuần ({teacher_count}).")
    else:
        st.session_state.sessions.append((cls, subj, teacher, count))
        st.success(f"Đã thêm: {cls} - {subj} ({teacher}, {count} buổi)")

if st.button("🗑️ Xóa tất cả"):
    st.session_state.sessions = []

if st.session_state.sessions:
    st.write("### Danh sách buổi học đã nhập")
    st.table(st.session_state.sessions)

iterations = st.number_input("Số lần lặp (iterations)", min_value=100, max_value=20000, value=2000, step=100)
restarts = st.number_input("Số lần restart", min_value=1, max_value=200, value=20, step=1)

if st.button("🔄 Sinh lịch khoa CNTT"):
    if not st.session_state.sessions:
        st.warning("⚠️ Bạn chưa nhập dữ liệu!")
    else:
        try:
            best_schedule, score = random_restart_hill_climbing(st.session_state.sessions, restarts, iterations)
            st.success(f"🎯 Điểm đánh giá: {score}")

            data = []
            for ca in cas:
                row = []
                for d in days:
                    cell_list = best_schedule.get((d, ca), [])
                    text = "\n".join([f"{s['class']} - {s['subject']} ({s['teacher']}, {s['room']})" for s in cell_list])
                    row.append(text)
                data.append(row)

            df = pd.DataFrame(data, index=cas, columns=days)
            st.write("### Lịch học khoa CNTT")
            st.dataframe(df, height=500, use_container_width=True)
        except ValueError as e:
            st.error(str(e))
