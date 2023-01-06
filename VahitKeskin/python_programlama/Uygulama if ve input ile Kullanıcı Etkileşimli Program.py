# mini uygulama

sinir = 50000
magaza_adi = input("Magaza Adi Nedir?")
gelir = int(input("Gelirinizi Giriniz:"))


if gelir > sinir:
    print("Tebrikler: " + magaza_adi + " Promosyon Kazandınız")
elif gelir < sinir:
    print("Uyarı! Cok dusuk gelir:" + str(gelir))
else:
    print("Takibe Devam")
