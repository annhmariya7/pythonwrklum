#syntax
# range(start,stop,step)              #step means how much increment/decrement       #stop is exclude to include use stop+1





# using for loop

#print numbers from low_limit to up_limit
low_limit=int(input("enter lower limit  "))
up_limit=int(input("enter upper limit  "))
for i in range(low_limit,up_limit+1):             #low_limit+1 used to include lower limit
    print(i)