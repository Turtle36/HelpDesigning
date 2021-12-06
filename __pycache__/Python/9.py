import sys

HARI = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')

nohari = int(input("masukkan nomor hari 1-7: "))
if (nohari < 1) or (nohari > 7):
    print("Tidak Ada Hari Ke-%s" % nohari)
    sys.exit(1)

print("Hari Ke-%s Adalah %s" % (nohari, HARI[nohari-1]))

