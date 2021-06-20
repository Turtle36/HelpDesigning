print(int(input("Masukkan Angka: ")))
a = [
    "Satu",
    "Dua",
    "Tiga",
    "Empat",
    "Lima",
    "Enam",
    "Tujuh",
    "Delapan",
    "Sembilan",
    "Sepuluh"]

i = input("Masukkan Angka: ")
for x in range(len(i)):
    print(a[int(i[x])-1], end=" ")
