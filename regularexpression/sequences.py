# from re import *

# text="abcd12kABC@#"

# pattern="\d"      #/d maens[0-9]
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.group(),m.start())


# from re import *

# text="abcd12kABC@#"

# pattern="\D"      #/D means[^0-9]
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.group(),m.start())



# from re import *

# text="abcd12kABC@#"

# #pattern="\w"      #\w means[alphanumeric means a-zA-Z0-9]
# pattern="\W"       #\W means special characters
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.group(),m.start())


from re import *
text="hellothere_@12"
#pattern="[b-df-hj-np-tv-z]"
pattern="[^aeiou]_\W\d"

matcher=finditer(pattern,text)

for m in matcher:
    print(m.group(),m.start())