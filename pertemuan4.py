nolist = []
genap = []
ganjil = []

data = int(input("Berapa banyak elemen dalam list : "))
for i in range(data):
    elm = int(input("Masukan nilai elemen : "))
    nolist.append(elm)

for j in range(data):
    if(nolist[j] % 2 == 0):
        genap.append(nolist[j])
    else:
        ganjil.append(nolist[j])
print()
print("Elemen - elemen dalam list : ", nolist)
print("Elemen ganjil dalam list : ", ganjil)
print("Elemen genap dalam list : ", genap)