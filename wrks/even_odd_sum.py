start=10
end=30

even_sum=0
odd_sum=0

while(start<=end):
    if start%2==0:
        even_sum=even_sum+start
    else:
        odd_sum=odd_sum+start
    start+=1
print("even sum:",even_sum)
print("odd sum:",odd_sum)