import streamlit as st
import datetime
import pandas as pd

# Konfigurasi Halaman Aplikasi Baru
st.set_page_config(
    page_title="Bio-Core Formalism - Advanced Molecular Synthesis",
    page_icon="⚛️",
    layout="centered"
)

st.title("⚛️ Bio-Core Formalism: Advanced Molecular Synthesis")
st.subheader("Engine Perancangan Bahan Aktif & Modul Formulasi Fisik Pelarut")

# Banner Info
st.info("💡 **R&D System:** Dilengkapi dengan modul kalkulasi bahan pembawa fisik (*Carrier/Solvent*) untuk panduan formulasi laboratorium.")

st.markdown("---")

# Inisialisasi Session State untuk Arsip Molekul Baru
if "arsip_molekul" not in st.session_state:
    st.session_state.arsip_molekul = []

# Panel Kontrol Parameter Utama & Ambang Batas
st.markdown("### 🎛️ Parameter Sintesis, Properti Kimiawi & Ambang Batas")

col1, col2 = st.columns(2)
with col1:
    nama_molekul_baru = st.text_input("Nama Kandidat Molekul Baru:", value="Bio-Core X-3")
    kategori_target = st.selectbox(
        "Target Spesifik Biologis Hama:",
        ["Insektisida (Sistemik Saraf)", "Fungisida (Inhibitor Dinding Sel)", "Herbisida (Blokir Enzim EPSPS)", "Bakterisida (Peptida Rekayasa)"]
    )
with col2:
    konstanta_zk = st.number_input("Konstanta Bio-Core ($Z_k$):", min_value=0.001, value=1.618033, step=0.000001, format="%.6f")
    tingkat_kerapatan = st.slider("Indeks Viskositas Informasi Ruang:", min_value=1.0, max_value=10.0, value=9.30, step=0.01)

col3, col4, col5 = st.columns(3)
with col3:
    fasa_a_info = st.number_input("Fasa Geometri Utama (A)", min_value=0.1, value=2.718, step=0.001, format="%.3f")
with col4:
    fasa_b_info = st.number_input("Fasa Viskositas Dasar (B)", min_value=0.1, value=0.900, step=0.001, format="%.3f")
with col5:
    skala_sintesis = st.number_input("Target Simulasi Massa (Gram)", min_value=10.0, value=500.0, step=50.0)

# Modul Pilihan Tipe Formulasi Fisik Pelarut
st.markdown("---")
st.markdown("### 🧪 Modul Formulasi Fisik & Pelarut (*Carrier/Solvent*)")
tipe_formulasi = st.selectbox(
    "Pilih Tipe Sediaan Formulasi Laboratorium:",
    ["Emulsifiable Concentrate (EC - Cairan Pekat Pelarut)", "Wettable Powder (WP - Serbuk Basah)", "Suspension Concentrate (SC - Pekatan Suspensi)"]
)

ambang_batas_validasi = st.slider(
    "🎯 Ambang Batas Kestabilan Lock-Binding (Minimum Threshold):", 
    min_value=10.0, 
    max_value=50.0, 
    value=24.5, 
    step=0.5
)

st.markdown("")

# Tombol Eksekusi Generator Molekul Baru
if st.button("🚀 Eksekusi Sintesis, Evaluasi & Kalkulasi Formulasi Fisik", use_container_width=True):
    
    # Perhitungan Matematika Berbasis Bio-Core Formalism & Kimiawi
    rasio_kinetik = fasa_a_info / fasa_b_info
    indeks_potensi_molekul = (rasio_kinetik * konstanta_zk) * tingkat_kerapatan
    titik_leleh_termal_prediksi = 125.4 + (indeks_potensi_molekul * 14.2)
    koefisien_ikatan_lock = (konstanta_zk ** 2) * (tingkat_kerapatan / fasa_b_info)
    
    # Parameter Kimiawi Tambahan
    prediksi_mw = round(150.0 + (fasa_a_info * 45.2) + (tingkat_kerapatan * 12.5), 2)
    prediksi_log_p = round(1.2 + (konstanta_zk * 1.5) - (fasa_b_info * 0.4), 2)
    estimasi_polar_surface_area = round(45.5 + (tingkat_kerapatan * 8.1), 2)
    
    # Kalkulasi Proporsi Bahan Fisik Berdasarkan Tipe Formulasi & Massa Total
    if "EC" in tipe_formulasi:
        massa_bahan_aktif = round(skala_sintesis * 0.20, 2)  # 20% Konsentrat Aktif
        massa_pelarut_utama = round(skala_sintesis * 0.65, 2) # 65% Pelarut Organik (Xylene/Aromatic Solvent)
        massa_surfaktan = round(skala_sintesis * 0.15, 2)     # 15% Emulsifier (Tween/Alkyl Aryl Polyglycol Ether)
        detail_pembawa = f"- Pelarut Utama: Aromatic Solvent ({massa_pelarut_utama} g)\n- Surfaktan/Emulsifier: Emulsifier Blend ({massa_surfaktan} g)"
    elif "WP" in tipe_formulasi:
        massa_bahan_aktif = round(skala_sintesis * 0.25, 2)  # 25% Konsentrat Aktif
        massa_pelarut_utama = round(skala_sintesis * 0.65, 2) # 65% Carrier Padat (Kaolin / Talkum)
        massa_surfaktan = round(skala_sintesis * 0.10, 2)     # 10% Wetting Agent (Sodium Lignosulfonate)
        detail_pembawa = f"- Carrier Padat: Kaolin/Talkum Halus ({massa_pelarut_utama} g)\n- Wetting Agent: Lignosulfonate ({massa_surfaktan} g)"
    else:
        massa_bahan_aktif = round(skala_sintesis * 0.30, 2)  # 30% Konsentrat Aktif
        massa_pelarut_utama = round(skala_sintesis * 0.55, 2) # 55% Carrier Cair (Air Demin / Propilen Glikol)
        massa_surfaktan = round(skala_sintesis * 0.15, 2)     # 15% Dispersing & Stabilizing Agent
        detail_pembawa = f"- Carrier Cair: Demineralized Water ({massa_pelarut_utama} g)\n- Dispersing Agent: Polimerik ({massa_surfaktan} g)"

    # Validasi Berdasarkan Ambang Batas Dinamis
    status_molekul = "VALID & STABIL (Informasi Terkunci Sempurna)" if koefisien_ikatan_lock >= ambang_batas_validasi else "KRITIS (Perlu Penyesuaian Viskositas)"

    # Simpan ke Session State Arsip
    waktu_eksekusi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_molekul_baru = {
        "Waktu": waktu_eksekusi,
        "Nama Molekul": nama_molekul_baru,
        "Formulasi": tipe_formulasi.split()[0],
        "Lock-Binding": round(koefisien_ikatan_lock, 3),
        "Status": status_molekul
    }
    st.session_state.arsip_molekul.insert(0, data_molekul_baru)

    st.markdown("---")
    st.subheader("🧬 Hasil Prediksi & Komposisi Formulasi Fisik")

    if "VALID" in status_molekul:
        st.success(f"STATUS SINTESIS: {status_molekul}")
    else:
        st.warning(f"STATUS SINTESIS: {status_molekul}")

    st.markdown("### 📊 Parameter Struktur Atomik & Kimiawi Terproyeksi:")
    st.markdown(
        f"* **Nama Kandidat:** `{nama_molekul_baru}`\n"
        f"* **Prediksi Bobot Molekul (MW):** `{prediksi_mw} g/mol`\n"
        f"* **Koefisien Partisi (Prediksi LogP):** `{prediksi_log_p}`\n"
        f"* **Luas Permukaan Polar (PSA):** `{estimasi_polar_surface_area} Å²`\n"
        f"* **Koefisien Kunci Molekuler (*Lock-Binding*):** `{koefisien_ikatan_lock:.3f}` *(Batas Min: {ambang_batas_validasi})*"
    )

    st.markdown("### ⚖️ Rincian Penimbangan Bahan Formulasi Lab (Skala Total: " + str(skala_sintesis) + " Gram):")
    st.markdown(
        f"* **Bahan Aktif ({nama_molekul_baru}):** `{massa_bahan_aktif} gram`\n"
        f"{detail_pembawa}"
    )

    # Fitur Unduh Dokumen Paten / Blueprint Molekul Baru
    st.markdown("---")
    st.subheader("📥 Unduh Blueprint & Resep Formulasi Lab")
    
    blueprint_konten = f"""==================================================
        BLUEPRINT & RESEP FORMULASI LABORATORIUM
        BIO-CORE FORMALISM - ADVANCED CHEMICAL ENGINE
==================================================
Tanggal & Waktu Laporan : {waktu_eksekusi}
Nama Kandidat Molekul   : {nama_molekul_baru}
Kategori Target Hama    : {kategori_target}
Tipe Sediaan Formulasi  : {tipe_formulasi}
Target Massa Total      : {skala_sintesis} Gram
--------------------------------------------------
PARAMETER STRUKTUR:
- Konstanta Utama (Z_k) : {konstanta_zk}
- Viskositas Informasi  : {tingkat_kerapatan}
- Koefisien Ikatan Lock : {koefisien_ikatan_lock:.3f}
- Status Validasi       : {status_molekul}
--------------------------------------------------
RINCIAN KOMPOSISI PENIMBANGAN FISIK:
1. Bahan Aktif          : {massa_bahan_aktif} gram
{detail_pembawa}
==================================================
CATATAN KEKAYAAN INTELEKTUAL:
Dokumen resep formulasi fisik ini diturunkan secara 
eksklusif berdasarkan kaidah Bio-Core Formalism Architecture.
================================================== """

    st.download_button(
        label="📄 Unduh Blueprint & Resep Lab (.txt)",
        data=blueprint_konten,
        file_name=f"Resep_Formulasi_{nama_molekul_baru.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
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
