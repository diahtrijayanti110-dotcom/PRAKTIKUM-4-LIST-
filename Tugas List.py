data = []

while True:
    print("\nNama : ", end="")
    nama = input()
    print("NIM  : ", end="")
    nim = input()
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    # Hitung nilai akhir
    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data.append([nama, nim, tugas, uts, uas, akhir])

    lanjut = input("Tambah data(y/t)?").lower()
    if lanjut == "t":
        break

# Tabel Header
print("=" * 78)
print("| {:<3} | {:<12} | {:<8} | {:<7} | {:<7} | {:<7} | {:<8} |".format(
    "No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
print("=" * 78)

# Tabel Isi
for i, d in enumerate(data, start=1):
    print("| {:<3} | {:<12} | {:<8} | {:<7} | {:<7} | {:<7} | {:<8.2f} |".format(
        i, d[0], d[1], d[2], d[3], d[4], d[5]
    ))

print("=" * 78)
