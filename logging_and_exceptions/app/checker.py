x=0
z= input("введите имя")
k=z.split(" ")
print(k)
for i in k:
     if 'A'<= i[0] <= 'Z' or 'А' <= i[0] <= 'Я':
         x+=1
     else:
         print("False")
print (x)