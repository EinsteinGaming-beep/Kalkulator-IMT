# pages/beranda.py

import streamlit as st

st.set_page_config(
    page_title="Kalkulator IMT",
    page_icon="🩸"
)
st.title("Selamat Datang di Kalkulator Indeks Massa Tubuh")
st.write("Website ini membantu Anda menghitung Indeks Massa Tubuh (IMT) dan memahami maknanya. IMT adalah alat sederhana untuk menentukan apakah seseorang memiliki berat badan yang sehat, kekurangan berat badan, kelebihan berat badan, atau obesitas.")

st.markdown("Kategori IMT
Berdasarkan nilai IMT, seseorang dapat dikategorikan ke dalam kelompok-kelompok berikut:
- Kurus (Kekurangan Berat Badan): IMT < 18,5
- Normal (Berat Badan Ideal): IMT 18,5 - 24,9
- Kelebihan Berat Badan: IMT 25 - 29,9
- Obesitas Tingkat 1: IMT 30 - 34,9
- Obesitas Tingkat 2: IMT 35 - 39,9
- Obesitas Tingkat 3 (Obesitas Morbid): IMT ≥ 40")
