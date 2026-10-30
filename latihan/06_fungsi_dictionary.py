# ==========================================
# PROGRAM: FUNGSI PENCARIAN
# ==========================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul(judul):
    print("=" * 40)
    print(judul.center(40))
    print("=" * 40)


# Fungsi untuk mencari data mahasiswa berdasarkan NIM
def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")


# Membuat dictionary data mahasiswa
mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "nilai": 85
    },
    "A002": {
        "nama": "Budi",
        "nilai": 78
    }
}

# Menampilkan judul program
tampilkan_judul("FUNGSI PENCARIAN")

# Mencari mahasiswa dengan NIM A002
print("Pencarian NIM A002:")
print(cari(mahasiswa, "A002"))

# Mencari mahasiswa dengan NIM A003
print("\nPencarian NIM A003:")
print(cari(mahasiswa, "A003"))