# Döngü ve Fonksiyonların Birlikte Kullanımı


def kare_al(x):
    print(x**2)


kare_al(2)

maaslar = [1000, 2000, 3000, 4000, 5000]

for i in maaslar:
    print(i)


# maaslara yuzde 20 zam yapilacak gerekli kodlari yaziniz

1000*20/100 + 1000

maaslar[0]*20/1000+maaslar[0]
maaslar[1]*20/1000+maaslar[1]
maaslar[2]*20/1000+maaslar[2]

# dongu yazilacak
# fonksiyon yazilacak


def yeni_maas(x):
    return x+x*20/100

yeni_maas(1000)
yeni_maas(2000)
yeni_maas(3000)

for i in maaslar:
    print(yeni_maas(i))