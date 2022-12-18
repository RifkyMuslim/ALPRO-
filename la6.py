import persegi
import segitiga

def tampilanMenu():
    print('Menu')
    print('1. Luas Segitiga')
    print('2. Keliling Segitiga')
    print('3. Luas Persegi')
    print('4. Keliling Persegi')
    print('5. Keluar')

def main():
    while True:
        tampilanMenu()
        pilihan = int(input('Masukan pilihan Anda: '))
        if pilihan == 1:
            alas = float(input('Masukan alas segitiga: '))
            tinggi = float(input('Masukan tinggi segitiga: '))
            print('Luas segitiga adalah', segitiga.luas(alas, tinggi))
        elif pilihan == 2:
            sisi = float(input('Masukan sisi segitiga: '))
            print('Keliling segitiga adalah', segitiga.keliling(sisi, sisi, sisi))
        elif pilihan == 3:
            sisi = float(input('Masukan sisi persegi: '))
            print('Luas persegi adalah', persegi.luas(sisi))
        elif pilihan == 4:
            sisi = float(input('Masukan sisi persegi: '))
            print('Keliling persegi adalah', persegi.keliling(sisi))
        elif pilihan == 5:
            print('Keluar dari program...')
            break
        else:
            print('Error: Pilihan tidak valid.')
        print()

main()  
