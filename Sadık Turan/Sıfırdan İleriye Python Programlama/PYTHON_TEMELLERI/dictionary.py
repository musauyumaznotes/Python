#key - value

sehirler = ["Kocaeli","İstanbul"]
plakalar =[41,34]

print(plakalar[sehirler.index("Kocaeli")])
print(plakalar[sehirler.index("İstanbul")])

plakalar = {"Kocaeli":41,"İstanbul" :34}
plakalar["Ankara"] = 6;

users = {
    "Musa Uyumaz" :{
        "age" :22,
        "roles":["admin","user"],
        "email":"musa@gmail.com",
        "adres":"Eskişehir",
        "phone" :"05654789632"
        },
    "Serhat Uyumaz" :17
}