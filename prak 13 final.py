# Nilai ujian
nilai_siswa = [90, 99, 97, 96, 98]

# Menghitung rata-rata nilai kelas
rata_rata_nilai_kelas = sum(nilai_siswa) / len(nilai_siswa)

# Menentukan siswa yang mendapatkan nilai di atas rata-rata kelas
nilai_di_atas_rata_rata = [nilai for nilai in nilai_siswa if nilai > rata_rata_nilai_kelas]

print(f"Rata-rata nilai kelas: {rata_rata_nilai_kelas:.2f}")
print(f"Siswa yang mendapatkan nilai di atas rata - rata: {nilai_di_atas_rata_rata}")
