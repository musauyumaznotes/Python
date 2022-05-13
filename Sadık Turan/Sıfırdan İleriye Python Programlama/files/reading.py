# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya Okuma Hatası")
# finally:
#     print("dosya kapandı")
#     file.close()

file = open("newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i,end="")
# file.close()

# read Fonksiyonu

# content = file.read()
# print(content)
# file.close()

# content = file.read(5)
# content = file.read(3)
# content = file.read(2)
# print(content)
# file.close()


# content = file.readline()
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# file.close()

# liste = file.readlines()
# print(liste)