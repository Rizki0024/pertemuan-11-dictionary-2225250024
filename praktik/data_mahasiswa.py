# ==================================================
# PROGRAM: SISTEM DATA MAHASISWA
# ==================================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul(judul):
    print("=" * 50)
    print(judul.center(50))
    print("=" * 50)


# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(data, nim):
    return data.get(nim)


# Fungsi untuk menghitung rata-rata nilai mahasiswa
def rata_rata_nilai(data):
    total = 0

    # Menjumlahkan seluruh nilai mahasiswa
    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    # Menghitung rata-rata nilai
    return total / len(data)


# Membuat dictionary data mahasiswa
# NIM digunakan sebagai key utama
data_mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "kelas": "A",
        "nilai": 85
    },
    "A002": {
        "nama": "Budi",
        "kelas": "A",
        "nilai": 78
    },
    "A003": {
        "nama": "Citra",
        "kelas": "B",
        "nilai": 92
    },
    "A004": {
        "nama": "Deni",
        "kelas": "B",
        "nilai": 74
    },
    "A005": {
        "nama": "Eka",
        "kelas": "A",
        "nilai": 88
    }
}


# ==================================================
# 1. PENCARIAN DATA MAHASISWA
# ==================================================

tampilkan_judul("PENCARIAN DATA MAHASISWA")

# Menentukan NIM yang ingin dicari
nim_dicari = "A003"

# Memanggil fungsi pencarian
hasil = cari_mahasiswa(data_mahasiswa, nim_dicari)

print("NIM yang dicari :", nim_dicari)

# Memeriksa apakah data ditemukan
if hasil is not None:
    print("Nama  :", hasil["nama"])
    print("Kelas :", hasil["kelas"])
    print("Nilai :", hasil["nilai"])
else:
    print("Data tidak ditemukan")


# ==================================================
# 2. PENCARIAN DATA TIDAK TERSEDIA
# ==================================================

tampilkan_judul("PENCARIAN DATA TIDAK TERSEDIA")

# Menentukan NIM yang tidak tersedia
nim_dicari = "A999"

# Memanggil fungsi pencarian
hasil = cari_mahasiswa(data_mahasiswa, nim_dicari)

print("NIM yang dicari :", nim_dicari)

# Menampilkan hasil pencarian
if hasil is not None:
    print("Nama  :", hasil["nama"])
    print("Kelas :", hasil["kelas"])
    print("Nilai :", hasil["nilai"])
else:
    print("Data tidak ditemukan")


# ==================================================
# 3. MENAMBAHKAN MAHASISWA BARU
# ==================================================

tampilkan_judul("MENAMBAHKAN MAHASISWA BARU")

# Menambahkan data mahasiswa baru ke dictionary
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

# Menampilkan informasi mahasiswa yang ditambahkan
print("Data mahasiswa berhasil ditambahkan")
print("NIM   : A006")
print("Nama  : Fajar")
print("Kelas : B")
print("Nilai : 80")


# ==================================================
# 4. MEMPERBARUI NILAI MAHASISWA
# ==================================================

tampilkan_judul("MEMPERBARUI NILAI MAHASISWA")

# Menentukan NIM dan nilai baru
nim_update = "A002"
nilai_baru = 82

# Memeriksa apakah NIM tersedia
if nim_update in data_mahasiswa:

    # Mengubah nilai mahasiswa
    data_mahasiswa[nim_update]["nilai"] = nilai_baru

    print("Nilai berhasil diperbarui")
    print("NIM        :", nim_update)
    print("Nilai baru :", data_mahasiswa[nim_update]["nilai"])

else:
    print("Data mahasiswa tidak ditemukan")


# ==================================================
# 5. MENAMPILKAN SELURUH DATA MAHASISWA
# ==================================================

tampilkan_judul("SELURUH DATA MAHASISWA")

# Menggunakan items() untuk mengambil key dan value
for nim, mahasiswa in data_mahasiswa.items():

    print("NIM   :", nim)
    print("Nama  :", mahasiswa["nama"])
    print("Kelas :", mahasiswa["kelas"])
    print("Nilai :", mahasiswa["nilai"])

    # Garis pemisah setiap data mahasiswa
    print("-" * 50)


# ==================================================
# 6. MENGHITUNG RATA-RATA NILAI
# ==================================================

tampilkan_judul("RATA-RATA NILAI MAHASISWA")

# Memanggil fungsi rata-rata nilai
rata_rata = rata_rata_nilai(data_mahasiswa)

# Menampilkan jumlah mahasiswa dan rata-rata nilai
print("Jumlah mahasiswa :", len(data_mahasiswa))
print("Rata-rata nilai  :", f"{rata_rata:.2f}")


# ==================================================
# 7. MEMERIKSA DATA MAHASISWA BARU
# ==================================================

tampilkan_judul("PEMERIKSAAN DATA MAHASISWA BARU")

# Mencari mahasiswa dengan NIM A006
hasil = cari_mahasiswa(data_mahasiswa, "A006")

# Memeriksa apakah data berhasil ditambahkan
if hasil is not None:

    print("Data mahasiswa A006 berhasil ditemukan")
    print("Nama  :", hasil["nama"])
    print("Kelas :", hasil["kelas"])
    print("Nilai :", hasil["nilai"])

else:
    print("Data mahasiswa A006 tidak ditemukan")