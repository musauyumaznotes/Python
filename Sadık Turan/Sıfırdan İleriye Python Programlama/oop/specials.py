myList = [1,2,3]
myString ="My String"
print(len(myList))
print(len(myString))


class Movie():
    def __init__(self,title,director,duration):
        self.director = director
        self.title = title
        self.duration = duration
        print("Movie Objesi Oluşturuldu")

m = Movie("Film Adı","Yönetmen","Filmin Süresi")

# print(len(m))