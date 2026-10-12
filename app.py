import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 2. Tạo dữ liệu
du_lieu = {
    "Ho_ten": ["An", "Bình", "Chi", "Dũng", "Hà", "Lân", "Minh", "Nam", "Phúc", "Trang"],
    "Chuyen_can": [9.0, 8.5, 7.0, 10.0, 8.0, 6.0, 9.0, 7.5, 8.0, 10.0],
    "Giua_ky": [7.5, 8.0, 6.0, 9.0, 7.0, 5.5, 8.5, 6.5, 7.5, 9.5],
    "Cuoi_ky": [8.0, 8.5, 6.5, 9.5, 7.5, 6.0, 8.5, 7.0, 7.5, 9.5]
}
df = pd.DataFrame(du_lieu)

# Tính điểm tổng kết & xếp loại
df["Tong_ket"] = (df["Chuyen_can"] * 0.2 + df["Giua_ky"] * 0.3 + df["Cuoi_ky"] * 0.5).round(2)

def xep_loai(diem):
    if diem >= 8.5: return "Giỏi"
    elif diem >= 7.0: return "Khá"
    elif diem >= 5.0: return "Trung bình"
    else: return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 3. Hiển thị Bảng điểm
st.subheader("Bảng điểm sinh viên")
st.dataframe(df)

# 4. Hiển thị Thống kê
st.subheader("Thống kê")
st.write(f"- Điểm trung bình lớp: **{round(df['Tong_ket'].mean(), 2)}**")

sv_max = df.loc[df["Tong_ket"].idxmax()]
st.write(f"- Điểm cao nhất: **{sv_max['Ho_ten']}** ({sv_max['Tong_ket']} điểm)")

sv_min = df.loc[df["Tong_ket"].idxmin()]
st.write(f"- Điểm thấp nhất: **{sv_min['Ho_ten']}** ({sv_min['Tong_ket']} điểm)")

so_dat = (df["Tong_ket"] >= 5.0).sum()
st.write(f"- Số sinh viên đạt: **{so_dat}/{len(df)}**")

# 5. Chọn sinh viên xem chi tiết
st.subheader("Chọn sinh viên xem chi tiết")
ten_sv = st.selectbox("Họ và tên:", df["Ho_ten"])
sv_info = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write(f"- Chuyên cần: {sv_info['Chuyen_can']}")
st.write(f"- Giữa kỳ: {sv_info['Giua_ky']}")
st.write(f"- Cuối kỳ: {sv_info['Cuoi_ky']}")
st.write(f"- Tổng kết: **{sv_info['Tong_ket']}**")
st.write(f"- Xếp loại: **{sv_info['Xep_loai']}**")

# 6. Biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots()
ax.bar(df["Ho_ten"], df["Tong_ket"], color="skyblue")
ax.set_xlabel("Sinh viên")
ax.set_ylabel("Điểm tổng kết")
st.pyplot(fig)

# 7. Thông tin cá nhân ở cuối trang
st.caption("Họ và tên: [Nguyen Viet Xuan Phong] - MSSV: [040208010468]")
