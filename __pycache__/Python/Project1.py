def main():
    try:
        a =[
        ["Keyboard"],
        ["Python_3_"],
        ["Alam"],
        ["Udara"],
        ["Awan"],
        ["Air"],
        ["Pohon"],
        ["Rumah"],
        ["Laptop"],
        ["Matahari"]]
        kata = int(input("Masukkan Angka 1-10: "))
        print(a[kata-1])
    except(ValueError):
        print("ERROR: Anda Melakukan Kesalahan")
    except(IndexError):
        print("ERROR: '%s' Tidak ditemukan")
if __name__ == '__main__':
    main()














































































