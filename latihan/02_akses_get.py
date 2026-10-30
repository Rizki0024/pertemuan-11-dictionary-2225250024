# ==========================================
# PROGRAM: AKSES AMAN DENGAN GET()
# ==========================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul(judul):
    print("=" * 40)
    print(judul.center(40))
    print("=" * 40)


# Menampilkan judul program
tampilkan_judul("AKSES DATA DENGAN GET()")

# Membuat dictionary data mahasiswa
data = {
    "nama": "Ayu",
    "nilai": 85
}

# Mengakses key yang tersedia
print("Nama Mahasiswa :", data.get("nama"))

# Mengakses key yang belum tersedia
# Jika tidak ditemukan, tampilkan "Belum ada"
print("Kelas           :", data.get("kelas", "Belum ada"))
