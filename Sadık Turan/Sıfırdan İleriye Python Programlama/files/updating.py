# with open("newfile.txt","r+",encoding="utf-8") as file:

#     print(file.read())
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     print(file.write("deneme"))

# with open("newfile.txt","a",encoding="utf-8")as file :
#     file.write("\nEmele Turan")
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())


# with open("newfile.txt","r+",encoding="utf-8") as file :
#     content = file.read()
#     content = "Efe Turan\n"+content
#     file.seek(0)
#     file.write(content)
#     print(file.read())
with open("newfile.txt","r+",encoding="utf-8") as file :
    list = file.readlines()
    list.insert(1,"Ali Korkmaz")
    print(list)