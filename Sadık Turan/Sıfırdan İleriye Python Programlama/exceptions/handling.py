# try:
#     x = input("x :")
#     y = input("y :")
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print("yanlış bilgi girdiniz")
#     print(e)
# except ValueError:
#     print("x ve ye için sayısal değer girmelisiniz")

# try:
#     x = input("x :")
#     y = input("y :")
#     print(x/y)
# except:
#     print("yanlış bilgi girdiniz")
while True:
    try:
        x = input("x :")
        y = input("y :")
        print(x/y)
    except Exception as ex:
        print("yanlış bilgi girdiniz ",ex)
    else:
        print("herşey yolunda")
        break
    finally:
        print("Try except sonlandı")