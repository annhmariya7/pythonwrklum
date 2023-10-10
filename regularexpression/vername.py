# starting with an alphabet k,l,m
#second place that must be a digit & that digit must be / by 3
#followed by any number of character


#answers of above three questions:
from re import *
variable=input("enter variable name ")
rule="[klm][369][/w]*"
matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")