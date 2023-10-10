start=10
end=20

#print total sum of all odd numbers & even nos from given start to end range

even_sum=0
odd_sum=0
while(start<=end):
    if(start%2==0):
        even_sum=even_sum+start
    else:
        odd_sum=odd_sum+start
    start+=1
print("even_sum" ,even_sum)
print("odd_sum",odd_sum)