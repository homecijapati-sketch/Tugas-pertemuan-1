# p1_diskon_hendri_if2022021.py

total_belanja = float(input("Masukkan total belanja: "))

if total_belanja >= 500000:
    diskon = 0.2 * total_belanja
elif total_belanja >= 250000:
    diskon = 0.1 * total_belanja
else:
    diskon = 0

total_bayar = total_belanja - diskon

print("Diskon:", diskon)
print("Total bayar:", total_bayar)