# ==========================================
# PROGRAM: DASAR DICTIONARY
# ==========================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul(judul):
    print("=" * 40)
    print(judul.center(40))
    print("=" * 40)


# Menampilkan judul program
tampilkan_judul("DASAR DICTIONARY")

# Membuat dictionary yang berisi data mahasiswa
data = {
    "nim": "A001",
    "nama": "Ayu",
    "nilai": 85
}

# Menampilkan data berdasarkan key
print("Data Mahasiswa")
print("NIM   :", data["nim"])
print("Nama  :", data["nama"])
print("Nilai :", data["nilai"])