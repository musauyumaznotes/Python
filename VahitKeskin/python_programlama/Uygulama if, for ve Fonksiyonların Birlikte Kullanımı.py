# mini uygulama
#Uygulama: if, for ve Fonksiyonların Birlikte Kullanımı

maaslar = [1000,2000,3000,4000,5000]


def zam_yap(zamOrani,maas):
    maas+= maas*zamOrani/100
    return maas

for i in maaslar:
    if i >= 3000:
        print(zam_yap(10, i))
    else:
        print(zam_yap(20, i) )
