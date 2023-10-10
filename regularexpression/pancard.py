from re import *
pan_id=input("enter pancard")
rule="[A-Z]{3}[PFACHT][A-Z][\d]{4}[A-Z]"
matcher=fullmatch(rule,pan_id)
print("in valid" if matcher==None else "valid") 



#pancard rules:
#1st three characters must be any random uppercase alphabets
#in 4th palce P or F or A or C or H or T
#in 5th place a randon uppercase alphabet
#4 digits
#last palce one random alphabet