names = ["Ali","Yağmur","Hakan","Deniz"]
years =[1998,2000,1998,1987]

#Cenk Liste sonunda ekle
# names.append("Cenk")

#Sena Liste başına ekle
# names.insert(0,"Sena") 
# names.insert(len(names),"Mehmet") 

#Denizi Sil
#names.pop(4)
# names.remove("Deniz")
# result = names.remove(-1)

#Deniz index numarası kaç
# result = names.index("Deniz")

#Ali Liste Elemanı mı?
# result = "Ali" in names

#Listeyi ters çevir
# result = names.reverse()
# result = names

#listeyi alfabetik sırala
# result = names.sort()
# result = names
 
#years listesini sırala
result = years.sort()
result = years

#str ="Chevrolet,Dacia" listeye çevir
# string ="Chevrolet,Dacia"
# result = string.split(",")

#en büyük ve enküçük eleman years
result = min(years)
result = max(years)

#kaç tane 1998 var years
result = years.count(1998)

#tüm elemanları sil years
# years.clear()

#kullanıcıdan alacağını 3 markayı listeye ekleyin
markalar=[]
marka =input("marka: ")
markalar.append(marka)
marka =input("marka: ")
markalar.append(marka)
marka =input("marka: ")
markalar.append(marka)

print(markalar)