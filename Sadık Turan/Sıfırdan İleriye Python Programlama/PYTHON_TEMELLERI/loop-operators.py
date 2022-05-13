#Range************
# list1 = [1,2,3]

# for item in range(50,100,20):
#     print(item)

# print(list(range(5,100,20)))

#Enumarate************** 
# greeting = "Hello There"
# index =0


# for letter in greeting:
#     print(f"index : {index} letter:{letter}")
#     index+=1

# for index,letter in enumerate(greeting):
#     print(f"index : {index} letter:{letter}")

#Zip******************
list1 =[1,2,3,4,5]
list2 =["a","b","c","d","e"]
list3 =[100,200,300,400,500]

print(list(zip(list1, list2,list3)))

for a,b,c in zip(list1,list2 ,list3):
    print(a,b,c)