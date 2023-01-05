# Fonksiyon Çıktılarını Girdi Olarak Kullanmak: return

def direk_hesap(isi, nem, sarj):
    print((nem+isi)/sarj)


cikti = direk_hesap(25, 40, 70)
cikti

print(cikti)
direk_hesap(25, 40, 70)*9


def direk_hesap(isi, nem, sarj):
    return (nem+isi)/sarj


cikti = direk_hesap(25, 40, 70)
cikti
print(cikti)
direk_hesap(25, 40, 70)*9


def direk_hesap(isi, nem, sarj):
    return
    (nem+isi)/sarj
