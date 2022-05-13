sayi = int(input("Sayi Giriniz:"))
i=2

if(sayi==1):
      print(f"{sayi} : Asal Sayı Değildir")

while i<sayi :
    if(sayi%i==0):
        print(f"{sayi} : Asal Sayı Değildir")
        break
    else:
        print(f"{sayi} : Asal sayıdır")
        break

for i in range(2,sayi):
    if(sayi%i==0):
        print(f"{sayi} : Asal Sayı Değildir")
        break
    else:
        print(f"{sayi} : Asal sayıdır")
       


