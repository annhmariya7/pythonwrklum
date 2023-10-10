from re import *

variable=input("enter variable>:")

rule="[a-zA-Z][\w]*"
matcher=fullmatch(rule,variable)

print("valid" if matcher!=None else "invalid")