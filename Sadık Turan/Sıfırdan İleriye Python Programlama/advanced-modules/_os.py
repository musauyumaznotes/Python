from datetime import datetime
import os

result = dir(os)
result = os.name
# Dizin Değiştirme
# os.chdir("C:\\")
# result = os.getcwd()

# Klasör Oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")


# Etkin dizin öğrenme
# result = os.getcwd()

# Listeleme
# result = os.listdir()
# result = os.listdir("C:\\")

result = os.stat("date.py")
# result = os.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) Oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) değiştirilme tarihi

# os.system("notepad.exe")

# path
# result = os.path.abspath("_os.py")
# result = os.path.dirname("C:\Users\musau\Desktop\BTK_AKADEMI\Sıfırdan İleriye Python Programlama\advanced-modules\_os.py")
# result = os.path.dirname(os.path.abspath("_os.py"))
# result = os.path.exists("_os.py")
# result = os.path.isdir("_os.py")
# result = os.path.isfile("_os.py")
# result = os.path.join("C:\\","deneme","deneme1")
# result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")


print(result)