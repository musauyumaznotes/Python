'''
    **Uygulamamızda 1-100 arasında rastgele sayı üretilecek sayıyı bulmaya çalışın 
    **random modülünü araştırın
    **100 üzerinden puanlama yap her soru 20 puan
    **Hak bilgisini kullanıcıdan al her soruda belirtilen can sayısı üzerinden hesaplansın
'''
can = int(input("Kaç Seferde Bilebilirsiniz :"))
import random
sayi = random.randint(1,100)
tahmin =0;
while can >= 0:
    can-=1
    tahmin = int(input("Tahmininizi Yazın :"))
    if(sayi>tahmin):
        print("Sayi {tahmin}'den Daha Büyük")
    elif(sayi<tahmin):
        print("Sayi {tahmin}'den Daha Küçük")
    elif(sayi==tahmin):
        print("Tebrikler Doğru Tahmin Ettiniz Bune Zeka Maşallah")
        break
    

if(can <=0):
    print(f"Sayımız:{sayi} Maalesef Bilemediniz Hakkınız Bitti Tekrar Denemek İster Misiniz")
