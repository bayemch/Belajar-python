"""
Materi 02: Operator dan Percabangan (if / elif / else)
Tanggal: 20 November 2026
"""

# ============================================================
# 1. OPERATOR ARITMATIKA
# ============================================================
a = 17
b = 5

print(a + b)    # 22  penjumlahan
print(a - b)    # 12  pengurangan
print(a * b)    # 85  perkalian
print(a / b)    # 3.4 pembagian (hasil selalu float)
print(a // b)   # 3   pembagian bulat (dibulatkan ke bawah)
print(a % b)    # 2   modulus (sisa bagi)
print(a ** b)   # 1419857 pangkat

# Kegunaan % : cek genap/ganjil
angka = 10
print(angka % 2 == 0)   # True berarti genap

# Operator penugasan singkat
x = 10
x += 5    # sama dengan x = x + 5  -> 15
x -= 3    # 12
x *= 2    # 24
print(x)

# ============================================================
# 2. OPERATOR PERBANDINGAN (hasilnya selalu True / False)
# ============================================================
print(5 == 5)    # sama dengan
print(5 != 3)    # tidak sama dengan
print(5 > 3)     # lebih besar
print(5 <= 3)    # lebih kecil atau sama dengan

# PERHATIAN: = untuk menyimpan nilai, == untuk membandingkan!

# ============================================================
# 3. OPERATOR LOGIKA: and, or, not
# ============================================================
umur = 20
punya_ktp = True

print(umur >= 17 and punya_ktp)   # True hanya jika KEDUANYA True
print(umur < 17 or punya_ktp)     # True jika SALAH SATU True
print(not punya_ktp)              # membalik: True -> False

# ============================================================
# 4. PERCABANGAN: if / elif / else
# ============================================================
# PENTING: Python memakai indentasi (4 spasi) untuk menandai blok kode.
nilai = 82

if nilai >= 85:
    print("Grade A")
elif nilai >= 70:
    print("Grade B")
elif nilai >= 55:
    print("Grade C")
else:
    print("Grade D")

# Python mengecek dari atas ke bawah dan berhenti di kondisi
# pertama yang True. Jadi urutan kondisi itu penting!

# if bersarang (nested)
umur = 19
punya_sim = False

if umur >= 17:
    if punya_sim:
        print("Boleh mengemudi")
    else:
        print("Belum punya SIM")
else:
    print("Belum cukup umur")

# ============================================================
# 5. CONTOH LENGKAP: program cek kelulusan
# ============================================================
nama = input("Nama: ")
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

rata_rata = (nilai_uts + nilai_uas) / 2

if rata_rata >= 60:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print(f"{nama}, rata-rata kamu {rata_rata:.1f} -> {status}")

# ============================================================
# 6. LATIHAN (kerjakan sendiri!)
# ============================================================
# Latihan 1: Minta user memasukkan sebuah angka, lalu cetak
#            apakah angka itu GENAP atau GANJIL.
#
# Latihan 2: Buat program penentu tahun kabisat.
#            Aturan: habis dibagi 4 DAN (tidak habis dibagi 100
#            ATAU habis dibagi 400).
#            Contoh: 2024 kabisat, 1900 bukan, 2000 kabisat.
#
# Latihan 3 (tantangan): Buat kalkulator sederhana.
#            Minta dua angka dan satu operator (+, -, *, /),
#            lalu cetak hasilnya. Jika operator tidak dikenal atau
#            pembagian dengan nol, tampilkan pesan error.