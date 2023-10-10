# mailids=[]
# contacts=[]
#from data.txt using file reading & regular expressions

from re import *
f=open("C:/Users/ANNMARIYA/Desktop/pythonwork/regularexpression/data.txt")

phn_rule="\d{10}"
mail_rule="[\w]+@gmail.com"

phn_numbers=[]
mail_ids=[]

for line in f:
    words=line.rstrip("\n").split()
    for w in words:
        phn_matcher=fullmatch(phn_rule,w)
        email_matcher=fullmatch(mail_rule,w)
        if phn_matcher!=None:
            phn_numbers.append(w)
        elif email_matcher!=None:
            mail_ids.append(w)

print(phn_numbers)
print(mail_ids)


          
