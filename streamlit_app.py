import streamlit as st

# Tambahkan judul aplikasi
st.title('Aplikasi Web UMKM')

# Tampilkan tombol dengan ikon
if st.sidebar.button('Beranda'):
    st.header('Selamat datang di halaman Beranda')
    st.write('Ini adalah halaman Beranda')

# Tampilkan tombol dengan ikon
if st.sidebar.button('UMKM'):
    st.header('Selamat datang di halaman UMKM')
    st.write('Ini adalah halaman UMKM')

# Tampilkan tombol dengan ikon
if st.sidebar.button('Tentang'):
    st.header('Selamat datang di halaman Tentang')
    st.write('Ini adalah halaman Tentang')
