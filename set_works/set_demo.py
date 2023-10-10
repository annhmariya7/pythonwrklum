# st=set()

# st={10,20,30}
# print(st)

# st={10,20,30,10,20}
# print(st)

# st={10,20,30,10,20,"hello",True,"hai"}
# print(st)


#to avoid duplication in a list
# lst=[10,20,30,10,20]    
# st=set(lst)             #to avoid duplication use set   that is change list to set
# print(st)


# st={10,20,30}
# st.add(100)
# print(st)

# st.add("ann")
# print(st)



# union
st1={10,20,30}
st2={11,12,20,24,30}
# union_set=st1.union(st2)
# print(union_set)

# intersection_set=st1.intersection(st2)
# print(intersection_set)

difference_set=st1.difference(st2)
print(difference_set)