def biodata():
        print("Program Biodata Mahasiswa")
        print("---------------------")
        nama = input("Masukan nama anda =")
        kelas = input("Masukan kelas anda =")
        npm = input("Masukan NPM anda =")
        print

def luas_lingkaran():
        print("Program Menghitung Luas Lingkaran")
        print("----------------------")
        phi = 3.14
        jari2 =float(input("Masukan Jari - Jari Lingkaran ="))
        luas = phi + jari2 + jari2
        print(f'Luas Lingkaran adalah {luas:.2f} cm2')

def main():
        print("---------------------")
        print("     ACTIVITY 2     ")
        print("----------------------")
        biodata()
        print("----------------------")
        luas_lingkaran()
main()