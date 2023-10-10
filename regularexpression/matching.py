# from re import *

# text="abababcdab"
# #     0123456789

# matcher=finditer("ab",text)        #variable=any function name("pattern",from where search)   #finiter fn needs (2 parameters)
# count=0

# for m in matcher:
#     print(m.start())                #position of matching object   #0 2 4 8
#     print(m.group())                #matching object  #ab ab ab ab
#     count+=1
# print(count)





#find a digit in text
# from re import *

# text="abcdABCD7e9fk"
# #     0123456789....

# #digits merans 0 to 9

# matcher=finditer("[0-9]",text)      #0 to 9 in square bracket means either 0 or 1 or 2 or.....or 9    


# for m in matcher:
#     print(m.start(),m.group())     


#lowercase case
# from re import *

# text="abcdABCD7e9fk"
# #     0123456789....

# matcher=finditer("[a-z]",text)         


# for m in matcher:
#     print(m.start(),m.group())                
   



#uppercase
# from re import *

# text="abcdABCD7e9fk"
# #     0123456789....
# pattern="[A-Z]"

# matcher=finditer(pattern,text)         


# for m in matcher:
#     print(m.start(),m.group())   


# all paterns in one set
# from re import *

# text="abcdABCD7e9fk"
# #     0123456789....

# matcher=finditer("[a-z0-9A-Z]",text)      

# for m in matcher:
#     print(m.start(),m.group())                
   


#pattern="[^0-9]"      #^ means except



#to print only special characters       #then we can use carret^
# from re import *

# text="abcdABCD7e9fk_"
# #     0123456789....

# pattern="[^a-zA-Z0-9]"
# matcher=finditer(pattern,text)         


# for m in matcher:
#     print(m.start(),m.group())  


#to print the vowels
# from re import *

# text="abcdABCD7e9fk_"
# #     0123456789....

# pattern="[aeiouAEIOU]"
# matcher=finditer(pattern,text)         
# count=0

# for m in matcher:
#     print(m.start(),m.group()) 
#     count+=1
# print(count) 




from re import *
text="hellothere@12"
pattern="[^aeiou]"

matcher=finditer(pattern,text)
#[a],b,c,d,[e],f,g,h,[i],j,k,l,m,n,[o],p,q,r,s,t,[u],v,w,x,y,z

for m in matcher:
    print(m.group())


   
