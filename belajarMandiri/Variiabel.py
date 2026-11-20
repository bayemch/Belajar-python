"""
Materi 01: Variabel, input(), dan f-string
Tanggal: 20 November 2026
"""

# ============================================================
# 1. VARIABEL
# Variabel = "kotak" bernama untuk menyimpan nilai.
# ============================================================
nama = "Budi"          # str
umur = 18              # int
tinggi = 170.5         # float
mahasiswa = True       # bool

print(nama, umur, tinggi, mahasiswa)

# Cek tipe data pakai type()
print(type(nama))      # <class 'str'>
print(type(umur))      # <class 'int'>

# Aturan nama variabel:
# - boleh huruf, angka, underscore; tidak boleh diawali angka
# - case sensitive: nama != Nama
# - konvensi Python: snake_case  (nama_lengkap, bukan namaLengkap)
nama_lengkap = "Budi Santoso"

# ============================================================
# 2. INPUT
# input() SELALU menghasilkan string, jadi angka harus dikonversi.
# ============================================================
nama_user = input("Siapa namamu? ")
umur_user = int(input("Berapa umurmu? "))   # int() mengubah str -> int

# ============================================================
# 3. F-STRING (cara modern menggabungkan teks dan variabel)
# ============================================================
print(f"Halo, {nama_user}! Tahun depan umurmu {umur_user + 1} tahun.")

# Format angka desimal: :.2f = 2 angka di belakang koma
ipk = 3.456789
print(f"IPK kamu: {ipk:.2f}")

# ============================================================
# 4. LATIHAN (kerjakan sendiri di bawah ini!)
# ============================================================
# Latihan 1: Minta user memasukkan nama dan jurusan,
#            lalu cetak: "Halo <nama>, kamu kuliah di <jurusan>"
#
# Latihan 2: Minta user memasukkan dua angka,
#            cetak hasil penjumlahan, pengurangan, perkalian, pembagian.
#            (ingat: input() menghasilkan str, pakai float()/int())
#
# Latihan 3: Konversi suhu Celsius ke Fahrenheit.
#            Rumus: F = (C * 9/5) + 32

