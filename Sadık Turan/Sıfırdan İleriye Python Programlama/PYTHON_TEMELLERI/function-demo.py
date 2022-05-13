
#Kelime Kaç Kez yazılsın Fonksiyonu

# def kelimeYazdir(kelime,kacKezYazilsin):
    # print(kelime*kacKezYazilsin)


# kelimeYazdir("Musa",10)

#Gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon

# def listeYap(*params):
#     return params

# print(listeYap("musa","uyumaz",10,25,64))


# def asalSayiBul(sayi1,sayi2):
    
#    for sayi in range(sayi1,sayi2):
#        if sayi>1:
#            for i in range(2,sayi):
#                 if (sayi % i == 0):
#                    break
#                 else:
#                     print(sayi)
                 
                     
           

# sayi1 = input("Sayi 1:")
# sayi2 = input("Sayi 2:")


def tamBolenleriBul(sayi):
    tamBolenler =[]
    for x in range(1,sayi):
        if(sayi % x == 0):
            tamBolenler.append(x)
        else:
            continue
    return tamBolenler

print(tamBolenleriBul(36))

  
    
   

