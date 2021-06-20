import sys

print("Fawwaz Translate\n")
for i in range(2, 4):
    KAMUS = {
    'blue':'Biru',
    'house':'Rumah',
    'one':'Satu'
    }

    kata = input("Masukkan Kata Dalam Bahasa Inggris: ")

    if not (kata in KAMUS.keys()):
        print("'%s' Tidak Ditemukan Di Dalam Kamus" % kata)
        sys.exit(1)

    print("Arti Kata '%s' Adalah '%s'" % (kata, KAMUS[kata]))

















