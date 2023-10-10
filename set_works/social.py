all_users=["dhoni","sachin","kohli","rohit","sanju","padikkal"]

sanju_following=["padikkal","sachin"]

#print suggessions for sanju

# st1=set(all_users)
# st2=set(sanju_following)
# suggession_list=st1.difference(st2)
# print(suggession_list)


#or
# suggessions=set(all_users).difference(set(sanju_following))          #to take difference change list to set

#or
suggessions=list(set(all_users).difference(set(sanju_following)))     #to remove sanju so take again set to list

sanju_poss=suggessions.index("sanju")
suggessions.pop(sanju_poss)
print(suggessions)

