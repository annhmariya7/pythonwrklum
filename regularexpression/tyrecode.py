#3digits/2digitRtwodigit/digit min 2 max 3 digit one alphabet=>rule

from re import *
tyre_id=input("enter a tyre code ")
rule="\d{3}[/]\d{2}R\d{2}[/]/d{2,3}[A-Z]"
matcher=fullmatch(rule,tyre_id)
print("valid" if matcher!=None else "in valid")