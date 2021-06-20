def main():
    try:
        # Kotak
        a =[
        ["Satu"],
        ["Dua"],
        ["Tiga"],
        ["Empat"],
        ["Lima"],
        ["Enam"],
        ["Tujuh"],
        ["Delapan"],
        ["Sembilan"],
        ["Sepuluh"]]

        kata = int(input("Masukkan Angka 1-10: "))
        print(a[kata-1])
    except(ValueError):
        print("ERROR: Anda Melakukan Kesalahan")
    except(IndexError):
        print("ERROR: '%s' Tidak ditemukan Di Dalam Kotak Ini" % kata)
if __name__ == '__main__':
    main()

















