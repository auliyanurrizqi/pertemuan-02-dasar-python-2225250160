print("Kalkulator Koordinat")

x1 = float(input("Masukkan koordinat x1: "))
y1 = float(input("Masukkan koordinat y1: "))
x2 = float(input("Masukkan koordinat x2: "))
y2 = float(input("Masukkan koordinat y2: "))

jarak = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

print(f"Titik A      : ({x1:.2f}, {y1:.2f})")
print(f"Titik B      : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan    : dx={x2 - x1:.2f} dy={y2 - y1:.2f}")
print(f"Jarak A ke B : {jarak:.2f}")
print(f"Titik tengah : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")