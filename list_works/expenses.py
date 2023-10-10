expenses=[12000,13000,14000,5000,20000,22000]
#           0     1     2     3     4     5

# print(expenses[1])           #expenses of feb month

# for e in expenses:              #to print all expenses
#     print(e)




# for e in expenses:
#     if e>15000:
#         print(e)





#total expenses
# total=0
# for e in expenses:
#     total=total+e
# print(total)

#or
# total_expenses=sum(expenses)
# print(total_expenses)




#costly(highest) expense
# max_exp=0         #assume
# for e in expenses:           #take amount one by one from expenses
#     if e>max_exp:
#         max_exp=e
# print(max_exp,"is costly expense")

#or
max_exp=max(expenses)
print(max_exp)


#cheapest expense
# expenses=[12000,13000,5000,15000,20000,3000]
# min_exp=expenses[0]
# for e in expenses:              #take each expenses one by one
#     if e<min_exp:
#         min_exp=e
# print(min_exp)

#or
# min_exp=min(expenses)
# print(min_exp)








# lst=[20,200,11,201]
#lst[0]=20
#lst[1]=200

# for n in lst:
#     print(n)

# for i in range[0,4]:
