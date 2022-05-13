sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# sayilar listesini while ile yazdirin
# x=0
# while x<len(sayilar):
#     print(sayilar[x])
#     x+=1

# baslangic ve bitis degerlerini kullanicadan al aradaki tek sayiları ekrana yazdır
# baslangic=int(input("Başlangıç değerini girin :"))
# bitis=int(input("bitis değerini girin :"))
# while baslangic<=bitis:
#     if baslangic %2!=0:
#         print(baslangic)
#     baslangic+=1

# 1-100 arası sayıları azalan şeklinde yazdır
# bas = 100
# while bas >= 0:
#     print(bas)
#     bas -= 1


# kullanıcıdan alınan 5 sayıyı sıralı şekilde yazdır
# numbers = []
# i = 0
# while i<5:
#    sayi = int(input("Sayi Girin: "))
#    numbers.append(sayi)
#    i+=1
# numbers.sort()
# print(numbers)

# Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesinde saklayın
# urun sayısı kullanıcıya sor
# dictionary listesi yapısı(name,price) şeklinde olsun
# ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listele

urunler = []
adet = int(input("Kaç Ürün Ekleyeceksiniz:"))

i=0
while (i<adet):
    name = input("Ürün İsmini Girin :")
    price = input("Ürün Fiyatını Girin :")
    urunler.append({
        "name" :name,
        "price":price
    })
    i+=1
for x in urunler:
    print( f' Ürün Adı : {x["name"]} Ürün Fiyatı: {x["price"]} ₺')
    