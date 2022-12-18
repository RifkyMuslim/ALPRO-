def main():
    file = open("Rifky.txt", "w")

    nama  = input("Masukan nama        : ")
    kelas = input("Masukan kelas       : ")
    npm   = input("Masukan npm         : ")
    hobi  = input("Masukan hobi        : ")
    makan = input("Masukan kesukaan    : ")
    cita  = input("Masukan cita - cita : ")

    file.write(nama  + "\n")
    file.write(kelas + "\n")
    file.write(npm   + "\n")
    file.write(hobi  + "\n")
    file.write(makan + "\n")
    file.write(cita  + "\n")

    file.close()
    print("Data berhasil ditulis\n")
main()

def main():
    file = open("Rifky.txt", "r")

    isi_file = file.read()

    print(isi_file)

    file.close()
    print("Data berhasil dibaca\n")
main()