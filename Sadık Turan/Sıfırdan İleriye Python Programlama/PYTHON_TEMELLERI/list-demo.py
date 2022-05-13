# Bmw Mercedes Opel Mazda Elemanlı Dizi Oluşturun
arabalar = ["Bmw","Mercedes","Opel","Mazda"]

#Liste Kaç Elemanlı
print(len(arabalar))
result =arabalar[0]
result = arabalar[-1]
#Mazda Değerini Toyota ile Değiştirin
arabalar[-1] ="Toyota"
result =arabalar
#Mercedes listenin br elemanı mı?
result = "Mercedes" in arabalar
#Listenin -2 indeksindeki değeri
result = arabalar[-2]
#Lisetenin ilk üç elemanı
result = arabalar[0:3]
result = arabalar[:3]
result = arabalar[-2:]
#listenin son iki elemanı yerine Toyota ve Renault eklyin
arabalar[-2:] =["Toyota","Renault"]
result =arabalar
#Listenin üzerine Audi ile Nissan Ekle
result = arabalar + ["Audi","Nissan"]
#Listenin Son Elemanını sil
del arabalar[-1]
result = arabalar
#Liste ELemanlarını tersten yaz 
result = arabalar[::-1]
#studentA :Yiğit Bilgi 2010,(70,60,70)
#studentB :Sena Turan 1999,(70,60,70)
#studentC :Ahmet Turan 1998,(80,70,90)
studentA =["Yiğit","Bilgi",2010,[70,60,70]]
studentB =["Sena","Turan",1999,[80,80,70]]
studentC =["Ahmet","Turan",1998,[80,70,90]]
students =[studentA,studentB,studentC]
#Listeyi ekrana yazdır
result = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"

print(result)