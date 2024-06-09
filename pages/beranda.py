# pages/beranda.py

import streamlit as st

st.set_page_config(
    page_title="Kalkulator IMT",
    page_icon="🩸"
)
st.title("Selamat Datang di Kalkulator Indeks Massa Tubuh")
st.write("Website ini membantu Anda menghitung Indeks Massa Tubuh (IMT) dan memahami maknanya. IMT adalah alat sederhana untuk menentukan apakah seseorang memiliki berat badan yang sehat, kekurangan berat badan, kelebihan berat badan, atau obesitas.")

st.markdown("""Kategori IMT

Berdasarkan nilai IMT, seseorang dapat dikategorikan ke dalam kelompok-kelompok berikut:
0 = Kurus Tingkat Berat < 17
1 = Kurus Tingkat Ringan 17 - 18,5
2 = Normal 18,5 - 25
3 = Gemuk Tingkat Ringan 25 - 30
4 = Obesitas > 30""")
