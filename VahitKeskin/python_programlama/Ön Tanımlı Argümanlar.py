# Ön Tanımlı Argümanlar

# ?print


def carpma_yap(x, y=1):
    print(x*y)


carpma_yap(3, 4)

print("HELLO AI ERA", sep=" ", end="")


# Argumanlarin Siralanmasi

def carpma_yap(x, y=1):
    print(x*y)


carpma_yap(y=2, x=3)

carpma_yap(2, 3)
