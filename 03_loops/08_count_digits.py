#Quetsion 8
#count digits in a number

num = int(input("Enter a number:"))
count = 0
while num > 0:
    count = count + 1
    num = num // 10
print("Nmmber of digits=", count)    
