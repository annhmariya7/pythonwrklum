#find hcf     highest common factor

num1=int(input("enter a number"))
num2=int(input("enter a number"))

for i in range(1,(num2+1)):
    if(num1 %i==0) and(num2 %i==0):
        hcf=i
print(hcf)

#lcm  hw

