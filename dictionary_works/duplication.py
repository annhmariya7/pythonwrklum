lst1=[10,11,4,12]
lst2=[9,10,11,6]
#write an algorithm for printing  elements from an array (without using set(intersection))
#without using in

lst1.sort()
lst2.sort()

p1,p2=0,0
while(p1<len(lst1) and p2<len(lst2)):            #loop until last element at lst & 2nd list
    if lst1[p1]==lst2[p2]:
        print(lst1[p1])
        p1+=1
        p2+=1
    elif lst1[p1]<lst2[p2]:
        p1+=1
    else:
        p2+=1

