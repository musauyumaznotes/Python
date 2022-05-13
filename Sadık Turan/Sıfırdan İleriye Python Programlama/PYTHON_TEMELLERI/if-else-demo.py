# İsim yaş eğitim bilgisi kulanıcıdan al ehliyet durumunu kontrol et yas18 eğitim lise veya üniversite olmalı
# isim = input("Ad Soyad :").upper().strip()
# yas = int(input("Yaş:"))
# egitim =input("Eğitim Durumu:").lower().strip()

# if yas>=18 and (egitim=="lise" or egitim=="üniversite"):
#     print(f"{isim} Ehliyet alabilir")
# else:
#     print(f"{isim} Ehliyet alamaz")

# 2yazılı 1 sözlü notu al ortalama hesapla
# 0-24 =0
# 25-44=1
# 45-54=2
# 55-69=3
# 70-84=4
# 85-100=5
yazili1 = int(input("Yazılı 1:"))
yazili2 = int(input("Yazılı 2:"))
sozlu = int(input("Sözlü :"))
ortalama = (yazili1+yazili2+sozlu)/3

if 0 <= ortalama < 25:
    print(f"ortalama:{ortalama} sonuc: 0")
elif 25 <= ortalama < 45:
    print(f"ortalama:{ortalama} sonuc: 1")
elif 45 <= ortalama < 55:
    print(f"ortalama:{ortalama} sonuc: 2")
elif 55 <= ortalama < 70:
    print(f"ortalama:{ortalama} sonuc: 3")
elif 70 <= ortalama < 85:
    print(f"ortalama:{ortalama} sonuc: 4")
elif 85 <= ortalama <= 100:
    print(f"ortalama:{ortalama} sonuc: 5")

# Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre yap
# 1.bakim =1.yıl
# 2.bakım 2.yıl
# 3.bakım 3.yıl
# süre hesabını gün ay yıl şeklinde hesaplayınız
import datetime
tarih = (input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9) "))
tarih = tarih.split("/")
trafigeCikis = datetime.datetime(int(tarih[0],int(tarih[1]),int(tarih[2])))
simdi =datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
    print("1. Servis Aralığı")
elif days>365 and days<=365*2:
    print("2. Servis Aralığı")
elif days>365*2 and days<=36532:
    print("3. Servis Aralığı")
else:
    print("Hatalı Süre")