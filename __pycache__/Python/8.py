def main():
    try:
        print(int(input("Masukkan Angka: ")))
    except(ValueError):
        print("ERROR: Harus Angka")
        print()
        print(int(input("Masukkan Angka: ")))
        print("ERROR: Harus Angka")
if __name__ == '__main__':
    main()
















