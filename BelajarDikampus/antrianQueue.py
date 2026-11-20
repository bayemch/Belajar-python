# ==========================================
# 1. MEMBUAT ADT STACK & 5 NAMA DENGAN PUSH
# ==========================================
# Stack awal berupa list kosong
stack_mahasiswa = []

# Menambahkan 5 nama menggunakan fungsi push (di Python menggunakan .append())
stack_mahasiswa.append("Fahri")
stack_mahasiswa.append("Budi")
stack_mahasiswa.append("Citra")
stack_mahasiswa.append("Dewi")
stack_mahasiswa.append("Eko")

print("Stack setelah di-push 5 nama:", stack_mahasiswa)

# ==========================================
# 2. MENAMPILKAN NAMA TERATAS DENGAN PEEK
# ==========================================
# Peek melihat elemen paling atas tanpa menghapusnya (di Python menggunakan indeks -1)
nama_teratas = stack_mahasiswa[-1]
print(f"Nama teratas (peek): {nama_teratas}")

# ==========================================
# 3. MENGHAPUS DUA NAMA MENGGUNAKAN POP
# ==========================================
# Pop menghapus elemen paling atas (elemen terakhir yang masuk)
nama_dihapus_1 = stack_mahasiswa.pop() # Menghapus 'Eko'
nama_dihapus_2 = stack_mahasiswa.pop() # Menghapus 'Dewi'

print(f"Nama yang dihapus: {nama_dihapus_1} dan {nama_dihapus_2}")

# ==========================================
# 4. MENAMPILKAN JUMLAH ELEMEN TERSISA
# ==========================================
# Menggunakan fungsi len() untuk menghitung sisa elemen
jumlah_tersisa = len(stack_mahasiswa)
print(f"Jumlah elemen tersisa di stack: {jumlah_tersisa}")
print(f"Isi stack sekarang: {stack_mahasiswa}")



