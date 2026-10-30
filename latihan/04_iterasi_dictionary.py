# ==========================================
# PROGRAM: ITERASI DICTIONARY
# ==========================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul(judul):
    print("=" * 40)
    print(judul.center(40))
    print("=" * 40)


# Membuat dictionary data mahasiswa
data = {
    "nama": "Ayu",
    "nilai": 85,
    "kelas": "A"
}

# Menampilkan judul program
tampilkan_judul("ITERASI DICTIONARY")

# Menampilkan seluruh pasangan key dan value
print("Data Mahasiswa:")

for key, value in data.items():
    print(f"{key}: {value}")