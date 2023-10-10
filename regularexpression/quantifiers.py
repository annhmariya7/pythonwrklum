# from re import *
# text="aabbcaabdaaa"

# #quantifiers

# # pattern="a+"     #a+ means atleast one a or minimum one a
#                 # that is + means one or more tome occurence
                 
# pattern="a*"     #*means zero a or more than zero a 
#pattern="a?"      #minimum one                    
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.group(),m.start())




from re import *
phone=input("enter the phone number ")
rule="\d{10}"       #digit maximum 10

matcher=fullmatch(rule,phone)     #for exact match use fullmatch instead of finditer

if(matcher==None):
    print("invalid")
else:
    print("valid")
