# Girilen İki Sayıdan Hangisi Büyüktür
a = int(input("sayi Girin :"))
b = int(input("sayi Girin :"))

result = (a > b)
print(f'a: {a} b:{b} den büyüktür :{result}')
# Kullanıcıdan 2 Vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız Ortalama 50 veüstüyse geçti değilse kaldı
vize1 = int(input("Vize 1 Girin :"))
vize2 = int(input("Vize 2 Girin :"))
final = int(input("Final Girin :"))

ortalama = (((vize1+vize2)/2)*0.6) + (final*0.4)
result = (ortalama >= 50)
print(f'not ortalamanız : {ortalama} geçme durumunuz : {result}')
# Girilen bir sayının tek mi çift mi olduğunu yazdırın
a = int(input("sayi Girin :"))
result = a % 2 == 0

# Girilen sayi Pozitif mi negatif mi
a = int(input("sayi Girin :"))
result = (a > 0)

print(f"sayiniz : {a} pozitif mi : {result}")
# parola ve e mail bilgisini isteyip doğruluğunu kontrol edin
email = (input("emaili Girin :"))
parola = (input("şifreyi Girin :"))

result1 = email.strip()=="musa@gmail.com"
result2 = parola.strip()=="12345"
print("f emailniz : {email} dogrulugu : {result1} , sifreniz : {parola} dogrulugu : {result2}")

