# ==========================================
# PROGRAM: MANIPULASI DICTIONARY
# ==========================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul(judul):
    print("=" * 40)
    print(judul.center(40))
    print("=" * 40)


# Membuat dictionary data mahasiswa
data = {
    "nama": "Ayu",
    "nilai": 85
}

# Menampilkan data awal
tampilkan_judul("DATA AWAL")
print(data)


# Menambahkan key dan value baru
tampilkan_judul("MENAMBAHKAN DATA")

data["kelas"] = "A"

print("Data setelah ditambahkan:")
print(data)


# Mengubah value dari key nilai
tampilkan_judul("MENGUBAH NILAI")

data["nilai"] = 90

print("Data setelah nilai diubah:")
print(data)


# Menghapus data menggunakan pop()
tampilkan_judul("MENGHAPUS DATA")

data.pop("kelas")

print("Data setelah kelas dihapus:")
print(data)