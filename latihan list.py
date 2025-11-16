
# Membuat list sebanyak 5 elemen dengan nilai bebas
A = [10, 20, 30, 40, 50]
print("Ini adalah Nilai list dariA()",A)

# --- Akses list ---
# Tampilkan elemen ke-3 (index 2)
print("Elemen ke-3:", A[2])

# Ambil nilai elemen ke-2 sampai ke-4 (index 1 sampai 3)
print("Elemen ke-2 sampai ke-4:", A[1:4])

# Ambil elemen terakhir
print("Elemen terakhir:", A[-1])

# --- Ubah elemen list ---
# Ubah elemen ke-4 (index 3) dengan nilai lain
A[3] = 99
print("Setelah mengubah elemen ke-4:", A)

# Ubah elemen ke-4 sampai elemen terakhir
A[3:] = [100, 200]   # contoh perubahan
print("Setelah mengubah elemen ke-4 sampai terakhir:", A)

# --- Tambah elemen list ---
# Ambil 2 bagian dari list A dan jadikan list B
B = A[:2]
print("List B:", B)

# Tambah list B dengan nilai string
B.append("Belajar")
print("List B setelah ditambah string:", B)

# Tambah list B dengan 3 nilai
B.extend([7, 8, 9])
print("List B setelah ditambah 3 nilai:", B)

# Gabungkan list B dengan list A
C = B + A
print("Hasil gabungan B dan A:", C)
