# Girilen sayı 0 100 aralığında mı
# sayi = int(input("Sayı Girin:"))
# result = sayi<100 and sayi>0
# print(f" {sayi} Sayisi 0 ile 100 arasındadır : {result}")

# Girilen sayı pozitif çift sayı mı
# sayi = int(input("sayı girin:"))
# result = sayi>0 and sayi%2==0
# print(f" {sayi} sayisi hem pozitif hem de çift sayidir : {result}")

# email parola bilgileri giriş kontrolü
# email = (input("Email Girin:"))
# sifre = (input("Şifre Girin:"))
# result = email=="musa@gmail.com" and sifre=="12345"
# print(f" {email} Hesabı sisteme girişi başarılı bir şekilde yapmıştır : {result}")

# girilen 3 sayıyı büyüklük olarak karşılaştır
# sayi1 = int(input("sayı girin:"))
# sayi2 = int(input("sayı girin:"))
# sayi3 = int(input("sayı girin:"))
# result1 = sayi1>sayi2 and sayi1>sayi3
# result2 = sayi2>sayi1 and sayi2>sayi3
# result3 = sayi3>sayi1 and sayi3>sayi2
# print(f" {sayi1} sayisi en büyüktür : {result1}")
# print(f" {sayi2} sayisi en büyüktür : {result2}")
# print(f" {sayi3} sayisi en büyüktür : {result3}")

# kullanıcdan 2 vize ve final notu al ortalama 50 ise geçti
# vize1 = int(input("vize1 Girin:"))
# vize2 = int(input("vize2 Girin:"))
# final = int(input("final Girin:"))
# ortalama = ((vize1+vize2)/2)*0.6 + (final*0.6)
# result = ortalama>=50
# print(f" {ortalama} ortalama ile geçti mi? : {result}")

# a)ortalama 50 bile olsa final 50 değilse kalır
# result = ortalama>=50 and final>=50
# print(f" ortalama: {ortalama} ve final notu: {final} ile geçti mi? : {result}")

# b)final 70 ise ortalama önemli değil
# result = ortalama>=50 or final>=70
# print(f" {ortalama} ortalama ve final notu: {final} ile geçti mi? : {result}")

# kisinin ad,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayın
# kilo = int(input("Kilo:"))
# boy = int(input("Boy(cm):"))/100
# indeks = kilo/boy**2
# result1 = 0<=indeks<18.5
# result2 = 18.5<=indeks<25
# result3 = 25<=indeks<30
# result4 = 30<=indeks<35
# print(f"Vücut Kitle İndexi : {indeks} Zayıf mı?: {result1}")
# print(f"Vücut Kitle İndexi : {indeks} Normal mi?: {result2}")
# print(f"Vücut Kitle İndexi : {indeks} Fazla Kilolu mu?: {result3}")
# print(f"Vücut Kitle İndexi : {indeks} Obez(Şişman) mi?: {result4}")
# 0-18.4  =>Zayıf
# 18.5-24.9  =>Normal
# 25-29.9  =>Fazla Kilo
# 30-34.9  =>Şişman(obez)
