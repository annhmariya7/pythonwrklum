# def->keyword   sub->function_name(parameters)
# def sub(n1,n2):
#     return n1-n2       #normal


#we can use lambada to consize length of prgrm
# sub=lambda n1,n2:n1-n2     
# print(sub(10,2))


# def cube(n):                 
#     return n**3             #normal

# cube=lambda n:n**3
# print(cube(3))


# def max_two(n1,n2):
#      return n1 if n1>n2 else n2
    

# max_two=lambda n1,n2:n1 if n1>n2 else n2
# print(max_two(10,20))


# odd_even=lambda n:"odd" if n%2!=0 else "even"
# print(odd_even(6))


# length of word
# get_len=lambda w:len(w)
# print(get_len("annmariya"))



# def smart_hub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1


smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(4,8))