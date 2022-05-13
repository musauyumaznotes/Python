# ogrenciler ={
#     "120":{
#         "ad": "Ali",
#         "soyad" :"Yılmaz",
#         "telefon":"5320000001"
#     },
#     "125":{
#         "ad": "Can",
#         "soyad" :"Korkmaz",
#         "telefon":"5320000002"
#     },
#     "128":{
#         "ad": "Volkan",
#         "soyad" :"Yükselen",
#         "telefon":"5320000003"
#     },
# }
ogrenciler = {}
number = input("Öğrenci Numarasını Girin: ")
name = input("Öğrenci Adını Girin: ")
surname = input("Öğrenci Soyadını Girin: ")
phone = input("Öğrenci Telefonunu Girin: ")

# ogrenciler[number] ={
#     "Ad":name,
#     "Soyad":surname,
#     "Telefon":phone,
# }
ogrenciler.update({number :{
    "Ad":name,
    "Soyad":surname,
    "Telefon":phone,
}})
print(ogrenciler)