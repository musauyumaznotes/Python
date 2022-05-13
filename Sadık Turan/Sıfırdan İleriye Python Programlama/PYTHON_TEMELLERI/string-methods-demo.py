website ="http://www.sadikturan.com"
course ="Python Kursu: Baştan Sona Programlama Rehberiniz (40 saat)"

# ' Hello World ' baştaki ve sondaki boşlukları silin.
result = " Hello World ".strip();
result = " Hello World ".lstrip();
result = " Hello World ".rstrip();

result = website.lstrip("/:pth")
# 'www.sadikturan.com' sadikturan harici silin
"www.sadikturan.com".strip("w.moc")
# "course" tüm karakterleri küçük harf yapın
result = course.lower()
result =course.upper()
result =course.title()
# "website" içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count("a")
result = website.count("www")
result = website.count("www",0,10)
# "website" "www" ile başlayıp com ile bitiyor mu
result = website.startswith("www")
result = website.endswith("com")
# "website" icinde ".com" ifadesi  var mı
result = website.find("com",0,10)
result = website.find("Python")
result = website.rfind("Python")

result = website.index("com")
result = website.rindex("com")
# result = website.rindex("comm") # exception
# "course" içineki karakterler alfabetik mi?(isalpha,isdigit)
result = course.isalpha()
result = course.isdigit()
# "Contents" ifadesini satırda 50 karakter içine yerleştir sağ ve soluna * ekle 
result ="Contents".center(50,"*")
result ="Contents".ljust(50,"*")
result ="Contents".rjust(50,"*")
# course tüm boşlukları - ile değiştirin
result = course.replace(" ","-")
result = course.replace(" ","-",5)
result = course.replace(" ","")
# Hello World World u There olarak değiştir
result ="Hello World".replace("World","There")
#course boşluk karakterinen kelimeleri ayır
result = course.split(" ")