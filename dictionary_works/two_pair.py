# lst=[2,5,3,7]
# #     0 1 2 3

# sum=9

# lst.sort()
# # print(lst)

# low=0
# upper=len(lst)-1

# while(low<upper):
#     cur_sum=lst[low]+lst[upper]
#     if cur_sum==sum:
#         print("pairs",lst[low],lst[upper])
#         break
#     elif cur_sum<sum:
#         low+=1
#     else:
#         upper-=1


#to get all pairs
lst=[2,5,3,7,4]
#     0 1 2 3

sum=9

lst.sort()
# print(lst)

low=0
upper=len(lst)-1

while(low<upper):
    cur_sum=lst[low]+lst[upper]
    if cur_sum==sum:
        print("pairs",lst[low],lst[upper])
        low+=1
    elif cur_sum<sum:
        low+=1
    else:
        upper-=1

