def menulisData():
    file = open('Rifky.txt', 'w')
    
    print('-----Menulis Data-----')
    nama  = input('Masukkan nama         : ')
    kelas = input('Masukkan kelas        : ')
    npm   = input('Masukkan NPM          : ')
    hobi  = input('Masukkan hobi         : ')
    makan = input('Makanan  kesukaan     : ')
    cita  = input('Masukkan cita - cita  : ')
    
    file.write(nama + '\n')
    file.write(kelas + '\n')
    file.write(npm + '\n')
    file.write(hobi + '\n')
    file.write(makan + '\n')
    file.write(cita + '\n')
    
    file.close()
    print("\n")
    print('Data berhasil ditulis ')
    print('--------------------')
    
def bacaData():
    file = open('Rifky.txt', 'r')
    
    isi_file = file.read()
    print('-----Baca Data-----')
    print(isi_file)
    
    file.close()
    print('Data berhasil dibaca\n')
    
def tambahData():
    file = open('Rifky.txt', 'a')
    
    print('-----Tambah Data-----')
    angka1 = int(input('Masukkan nilai UTS : '))
    angka2 = int(input('Masukkan nilai UAS : '))
    angka3 = int(input('Masukkan nilai UU  : '))
    
    file.write(str(angka1) + '\n')
    file.write(str(angka2) + '\n')
    file.write(str(angka3) + '\n')
    
    file.close()
    print('\n')
    print('Data berhasil ditambah\n')
    
def main():
    menulisData()
    tambahData()
    bacaData()
    
main()