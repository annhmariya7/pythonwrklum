# lst=[2,1,5,3,6,3,6]
# print duplicate numbers
# lst.sort()
# print(lst)
# for i in range(0,len(lst)-1):
#     current=lst[i]
#     next=lst[i+1]
#     if current==next:
#         print(current,"is duplicate number")


#or
lst=[2,1,5,3,6,3,6,6]               #here 6 duplicates 3 times 
# print duplicate numbers
lst.sort()
duplicate_list=[]
for i in range(0,len(lst)-1):
    current=lst[i]
    next=lst[i+1]
    if current==next:
        if current not in duplicate_list:
            duplicate_list.append(current)
print(duplicate_list)