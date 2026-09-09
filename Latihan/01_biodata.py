TAHUN_SEKARANG = 2026

nama=input("Nama: ")
nim=input("NIM: ")
kelas=input("Kelas: ")
tahun_lahir=int(input("Tahun lahir: "))

umur = TAHUN_SEKARANG - tahun_lahir

print()
print("Biodata")
print("Nama: ",nama)
print("NIM: ",nim)
print("Kelas: ",kelas)
print("Umur: ",umur,"tahun")