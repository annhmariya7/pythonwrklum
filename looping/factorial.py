num=int(input("enter number to find the factorial"))  #5

start=1
fact=1     #not use 0 bcz when multiply all numbers turns to zero
while(start<=num):
    fact=fact*start
    start+=1

print(fact)