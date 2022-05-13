MusaHesap ={
    "ad": "Musa Uyumaz",
    "hesapNo":"13245678",
    "bakiye":3000,
    "ekHesap":2000,
}
AliHesap ={
    "ad": "Ali Çelik",
    "hesapNo":"12345678",
    "bakiye":2000,
    "ekHesap":1000,

}

def paraCek(hesap):
    print(f"Merhaba {hesap['ad']} Bakiyeniz : {hesap['bakiye']}")
    cekilecekTutar = int(input("Kaç Tl Çekilecek :"))
    tumHesaplar = hesap['bakiye']+hesap['ekHesap']
    
    if(cekilecekTutar>hesap['bakiye']):
        paraCekilsinmi = input("Para Ek Hesaptan Çekilsin Mi(e/h) : ").lower()
        if(paraCekilsinmi == "e"):
            hesap['ekHesap'] = tumHesaplar - cekilecekTutar
            hesap['bakiye'] = 0
        else:
            print("Para Çekilme İşlemi İptal Edilmiştir Üzgünüz Bakiyeniz Yetersiz")
    else:
        hesap['bakiye']=hesap['bakiye']-cekilecekTutar

        

   
    print(f"Bakiyeniz : {hesap['bakiye']} Ek Hesabınız : {hesap['ekHesap']}")

def KontrolEtParaYeterliMi(toplamPara,miktar):
    if(miktar>toplamPara):
        print("Bakiye Yetersiz")
        return
        

paraCek(MusaHesap)

    

