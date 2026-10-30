# ==========================================
# PROGRAM: DICTIONARY BERSARANG
# ==========================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul(judul):
    print("=" * 40)
    print(judul.center(40))
    print("=" * 40)


# Membuat dictionary yang berisi dictionary
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
tampilkan_judul("DICTIONARY BERSARANG")

# Mengakses nama mahasiswa dengan NIM A001
print("Nama A001  :", mahasiswa["A001"]["nama"])

# Mengakses nilai mahasiswa dengan NIM A002
print("Nilai A002 :", mahasiswa["A002"]["nilai"])