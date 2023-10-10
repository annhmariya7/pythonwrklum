# rules for veh num:
#starting with=>    KL
#two digits
#alphabets minimum 1 max 2
#4 digits

from re import *
veh_id=input("enter a vehicle number ")
rule="(KL)-\d{2}-[A-Z]{1,2}-\d{4}"        #"[KL]" means either K or L "(KL)" means both K &L
matcher=fullmatch(rule,veh_id)
print("valid" if matcher!=None else "in valid")










