
# Pertemuan 11 - Dictionary/Map

**Nama:** Rizki Ramadan  
**NIM:** 2225250024  
**Kelas:** 3F

## 1. Tujuan

Mempelajari penggunaan dictionary dalam Python untuk
menyimpan dan mengelola data pendidikan berdasarkan
pasangan key-value.

Program ini dibuat untuk memahami cara mencari,
menambahkan, mengubah, dan menampilkan data mahasiswa
menggunakan dictionary.

## 2. Struktur Data

Program menggunakan dictionary dengan NIM sebagai
key utama.

Setiap mahasiswa memiliki tiga informasi, yaitu:
- Nama
- Kelas
- Nilai

Contoh struktur data:

```python
data_mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "kelas": "A",
        "nilai": 85
    }
}
```

NIM digunakan sebagai key agar data mahasiswa dapat
dicari secara langsung tanpa harus menggunakan indeks.

Program juga menggunakan dua fungsi, yaitu:
- cari_mahasiswa(data, nim): mencari data mahasiswa.
- rata_rata_nilai(data): menghitung rata-rata nilai.

## 3. Cara Menjalankan

1. Buka folder proyek melalui VS Code.
2. Buka file Python yang ingin dijalankan.
3. Buka terminal VS Code.
4. Jalankan perintah berikut:

```bash
python praktik/data_mahasiswa.py
```

Untuk menjalankan latihan, gunakan contoh:

```bash
python latihan/01_dasar_dictionary.py
```

## 4. Test Case

| Kasus | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Pencarian tersedia | A003 | Data Citra tampil | Data Citra tampil | Berhasil |
| Pencarian tidak tersedia | A999 | Data tidak ditemukan | Data tidak ditemukan | Berhasil |
| Pembaruan nilai | A002 menjadi 82 | Nilai menjadi 82 | Nilai menjadi 82 | Berhasil |
| Penambahan data | A006 | Data tersimpan | Data tersimpan | Berhasil |
| Rekap data | items() | Semua data tampil | Semua data tampil | Berhasil |

## 5. Refleksi

Dari latihan ini, saya memahami bahwa dictionary
dapat digunakan untuk menyimpan data berdasarkan
key sehingga pencarian menjadi lebih mudah.

Salah satu kesalahan yang perlu diperhatikan adalah
mengakses key yang belum tersedia karena dapat
menyebabkan KeyError.

Untuk menghindarinya, saya menggunakan get() agar
program tetap berjalan ketika data tidak ditemukan.

Saya juga memahami penggunaan items() untuk
menampilkan key dan value secara bersamaan, serta
penggunaan fungsi agar program lebih terstruktur.

## 6. Sumber dan Bantuan

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 11.
- Python Software Foundation - Python Documentation.
- Bantuan ChatGPT (OpenAI) untuk memahami materi,
  menyusun kode, dan memeriksa penyelesaian program.
