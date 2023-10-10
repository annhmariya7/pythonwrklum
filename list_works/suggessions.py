# all_users=["jaison","jini","antony","zabeth","liam","ann"]
#                 # 0      1       2       3       4      5
# ann_users=["jaison","antony","liam"]
# #suggessions for ann

# suggestion_list=[]                 #can remove ann from ann_users list use pop in list
# for e in all_users:
#     if e not in ann_users:
#         suggestion_list.append(e)
# suggestion_list.pop(suggestion_list.index("ann"))       #in pop we can onlu use index value
# print(suggestion_list)





#mutual friends find
zabeth_friends=["antony","jini","jaison"]
ann_users=["jaison","antony","liam"]
equliast=[]
for e in zabeth_friends:
    for j in ann_users:
        if e==j:
            equliast.append(e)
print(equliast)


#or

# mutual=[]
# for e in zabeth_friends:
#     if e in ann_users:
#         mutual.append(e)
# print(mutual)




        