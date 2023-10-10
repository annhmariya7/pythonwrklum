lst=[2,4,1,5]
# find least missing +ve integer

lst.sort()
for i in range(0,len(lst-1)):              #lst-1 means if no missing number then loop will go out of the loop & print an error
    current=lst[i]
    next=lst[i+1]
    diff=next-current
    if diff!=1:
        print(current+1,"is missing number")
        break
    