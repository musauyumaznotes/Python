liste =["1","2","5a","10b","abc","10","50"]

# Liste Elemanları içindeki sayısal değerleri bulun

# for x in liste:
#     try:
#         sayi = int(x)
#         print(sayi)
#     except:
#         print(f"{x} sayi değildir")

# for x in liste:
#     try:
#         sayi = int(x)
#         print(sayi)
#     except ValueError:
#         continue

# Kullanıcı q değerini girmediği sürece aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı veriniz
 
# while True:
#     veri = input("Sayi Giriniz : ")
#     if(veri=="q"):
#         break
#     try:
#         sayi = int(veri)
#         print(sayi)
#     except:
#         print(f"{veri} sayi değildir")

# girilen parola içinde türkçe karakter hatası verin

# import re
# parola = input("Parola girin : ")
# if(re.search("[Ü,ü,ı,İ,Ğ,ğ,ş,Ş,Ç,ç,ö,Ö]",parola)):
#     raise Exception(f"parola Türkçe karakter içeremez {parola}")
# else:
#     print(f"parola kurallara uyuyor : {parola}")

# faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verin

def faktoriyel(x):
    x = int(x)

    if x<0:
        raise ValueError("Negatif Değer Girilemez")

    result = 1

    for i in range(1,x+1):
        result *=i

    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)