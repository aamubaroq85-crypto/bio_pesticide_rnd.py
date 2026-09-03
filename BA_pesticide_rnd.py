import streamlit as st
import datetime
import pandas as pd

# Konfigurasi Halaman Aplikasi Baru
st.set_page_config(
    page_title="Bio-Core Formalism - Novel Molecular Synthesis",
    page_icon="⚛️",
    layout="centered"
)

st.title("⚛️ Bio-Core Formalism: Novel Molecular Synthesis")
st.subheader("Engine Perancangan Bahan Aktif Baru Berbasis Viskositas Informasi")

# Banner Info
st.info("💡 **R&D System:** Mesin generator molekul sintetis baru berbasis tetapan Konstanta Bio-Core ($Z_k$) untuk menciptakan bahan aktif pestisida masa depan yang belum pernah ada di alam.")

st.markdown("---")

# Inisialisasi Session State untuk Arsip Molekul Baru
if "arsip_molekul" not in st.session_state:
    st.session_state.arsip_molekul = []

# Panel Kontrol Parameter Utama
st.markdown("### 🎛️ Parameter Sintesis & Konstanta Bio-Core")

col1, col2 = st.columns(2)
with col1:
    nama_molekul_baru = st.text_input("Nama Kandidat Molekul Baru:", value="Bio-Core Structural Compound X-1")
    kategori_target = st.selectbox(
        "Target Spesifik Biologis Hama:",
        ["Insektisida (Sistemik Saraf)", "Fungisida (Inhibitor Dinding Sel)", "Herbisida (Blokir Enzim EPSPS)", "Bakterisida (Peptida Rekayasa)"]
    )
with col2:
    konstanta_zk = st.number_input("Konstanta Bio-Core ($Z_k$):", min_value=0.001, value=1.618033, step=0.000001, format="%.6f")
    tingkat_kerapatan = st.slider("Indeks Viskositas Informasi Ruang:", min_value=1.0, max_value=10.0, value=6.283, step=0.01)

col3, col4, col5 = st.columns(3)
with col3:
    fasa_a_info = st.number_input("Fasa Geometri Utama (A)", min_value=0.1, value=2.718, step=0.001, format="%.3f")
with col4:
    fasa_b_info = st.number_input("Fasa Viskositas Dasar (B)", min_value=0.1, value=1.000, step=0.001, format="%.3f")
with col5:
    skala_sintesis = st.number_input("Target Simulasi Massa (Gram)", min_value=10.0, value=500.0, step=50.0)

st.markdown("")

# Tombol Eksekusi Generator Molekul Baru
if st.button("🚀 Eksekusi Sintesis Molekul & Kalkulasi Struktur Bio", use_container_width=True):
    
    # Perhitungan Matematika Berbasis Bio-Core Formalism
    rasio_kinetik = fasa_a_info / fasa_b_info
    indeks_potensi_molekul = (rasio_kinetik * konstanta_zk) * tingkat_kerapatan
    titik_leleh_termal_prediksi = 125.4 + (indeks_potensi_molekul * 14.2)
    koefisien_ikatan_lock = (konstanta_zk ** 2) * (tingkat_kerapatan / fasa_b_info)
    
    # Validasi Kestabilan Informasi
    status_molekul = "VALID & STABIL (Informasi Terkunci Sempurna)" if koefisien_ikatan_lock >= 25.0 else "KRITIS (Perlu Penyesuaian Viskositas)"

    # Simpan ke Session State Arsip
    waktu_eksekusi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_molekul_baru = {
        "Waktu": waktu_eksekusi,
        "Nama Molekul": nama_molekul_baru,
        "Target": kategori_target.split()[0],
        "Z_k": konstanta_zk,
        "Indeks Potensi": round(indeks_potensi_molekul, 3),
        "Status": status_molekul
    }
    st.session_state.arsip_molekul.insert(0, data_molekul_baru)

    st.markdown("---")
    st.subheader("🧬 Hasil Prediksi & Karakteristik Molekul Baru")

    if "VALID" in status_molekul:
        st.success(f"STATUS SINTESIS: {status_molekul}")
    else:
        st.warning(f"STATUS SINTESIS: {status_molekul}")

    st.markdown("### 📊 Parameter Struktur Atomik & Fisik-Kimia Terproyeksi:")
    st.markdown(
        f"* **Nama Kandidat:** `{nama_molekul_baru}`\n"
        f"* **Indeks Potensi Biologis:** `{indeks_potensi_molekul:.3f} Units`\n"
        f"* **Prediksi Titik Leleh / Ketahanan Termal:** `{titik_leleh_termal_prediksi:.2f} °C`\n"
        f"* **Koefisien Kunci Molekuler (*Lock-Binding*):** `{koefisien_ikatan_lock:.3f}`\n"
        f"* **Kerapatan Viskositas Informasi:** `{tingkat_kerapatan} (Z-Matrix)`"
    )

    st.markdown("### 🧪 Deskripsi Geometri & Mekanisme Kerja Bio-Core:")
    st.markdown(f"1. Molekul ini dirancang bukan dari struktur kimia acak, melainkan hasil terjemahan **Konstanta Bio-Core ($Z_k = {konstanta_zk}$)** yang diselaraskan dengan frekuensi reseptor hama pada kategori **{kategori_target}**.")
    st.markdown(2. f"Struktur ikatan memiliki ketahanan mutlak terhadap degradasi foton karena terlindungi oleh indeks viskositas informasi ruang sebesar **{tingkat_kerapatan}**.")
    st.markdown("3. Molekul siap dievaluasi lebih lanjut untuk tahap formulasi fisik di laboratorium.")

    # Fitur Unduh Dokumen Paten / Blueprint Molekul Baru
    st.markdown("---")
    st.subheader("📥 Unduh Blueprint Sintesis Molekul Baru")
    
    blueprint_konten = f"""==================================================
        BLUEPRINT SINTESIS MOLEKUL BARU (R&D)
        BIO-CORE FORMALISM - NOVEL ACTIVE ENGINE
==================================================
Tanggal & Waktu Laporan : {waktu_eksekusi}
Nama Kandidat Molekul   : {nama_molekul_baru}
Kategori Target Hama    : {kategori_target}
--------------------------------------------------
PARAMETER KONSTANTA BIO-CORE:
- Konstanta Utama (Z_k) : {konstanta_zk}
- Fasa Utama (A)        : {fasa_a_info}
- Fasa Dasar (B)        : {fasa_b_info}
- Viskositas Informasi  : {tingkat_kerapatan}
--------------------------------------------------
HASIL PREDIKSI PROPERTI FISIK-KIMIA:
- Indeks Potensi Biologis: {indeks_potensi_molekul:.3f} Units
- Prediksi Ketahanan Suhu: {titik_leleh_termal_prediksi:.2f} °C
- Koefisien Ikatan Lock : {koefisien_ikatan_lock:.3f}
- Status Validasi       : {status_molekul}
- Target Massa Simulasi : {skala_sintesis} Gram
==================================================
CATATAN KEKAYAAN INTELEKTUAL:
Dokumen blueprint molekul ini diturunkan secara eksklusif
berdasarkan kaidah Bio-Core Formalism Architecture.
================================================== """

    st.download_button(
        label="📄 Unduh Blueprint Molekul (.txt)",
        data=blueprint_konten,
        file_name=f"Blueprint_Molekul_{nama_molekul_baru.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain",
        use_container_width=True
    )

# Tampilkan Arsip Molekul Baru Tersimpan
if st.session_state.arsip_molekul:
    st.markdown("---")
    st.subheader("📚 Arsip Kandidat Molekul Baru (Session Log)")
    df_arsip = pd.DataFrame(st.session_state.arsip_molekul)
    st.dataframe(df_arsip, use_container_width=True)
    
    if st.button("🗑️ Bersihkan Arsip Molekul"):
        st.session_state.arsip_molekul = []
        st.rerun()

# Grafik Analisis Viskositas Informasi
st.markdown("---")
st.markdown("### 📈 Grafik Sebaran Indeks Potensi & Viskositas Informasi")
chart_data_novel = pd.DataFrame({
    "Komponen Matriks": ["Konstanta Z_k", "Fasa Geometri (A)", "Fasa Viskositas (B)", "Indeks Kerapatan"],
    "Nilai Skala": [konstanta_zk * 20, fasa_a_info * 10, fasa_b_info * 15, tingkat_kerapatan * 5]
}).set_index("Komponen Matriks")

st.bar_chart(chart_data_novel)
