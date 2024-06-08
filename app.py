import streamlit as st
from multiapp import MultiApp
from pages import beranda, info, kalkulator_imt

app = MultiApp()

# Tambahkan semua aplikasi ke dalam MultiApp
app.add_app("Beranda", beranda.run)
app.add_app("Info", info.run)
app.add_app("Kalkulator IMT", kalkulator_imt.run)

# Jalankan aplikasi utama
app.run()
