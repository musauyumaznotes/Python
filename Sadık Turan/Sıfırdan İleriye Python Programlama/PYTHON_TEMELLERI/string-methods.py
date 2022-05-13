message =" Hello there My name is Musa Uyumaz"

message = message.upper()
message = message.lower()
message = message.title()

message = message.capitalize() 
message = message.strip() #Boşlukları Yok Etti
message = message.split() #Cümleyi Parçalara Ayırdı
message ='*'.join (message) 
index = message.find("Musa")
isFound = message.startswith('M')
isFound = message.endswith('n')
message = message.replace("Musa","MusaReis") 
message = message.center(100,"*") 


print(message)