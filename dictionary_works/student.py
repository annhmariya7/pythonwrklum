student={"roll":12,"name":"maria","course":"django"}
# print(student["course"])

# if "total" in student:
#     print("present")
# else:
#     print("not present")


# student["grade"]="A"              #adding a key to dictionary
# print(student)



#get()method
# print(student["salary"])     #prgrm will stop with an error    not print hello,hai      
#or
# print(student.get("salary"))          #prgrm will run with error & stop at end with hello & hai
print("hello")
print("hai")



#keys()method
# for k in student.keys():              #to print all keys in the dictionary
#     print(k)


#values()method
for v in student.values():
    print(v)


#items()method
for k,v in student.items():
    print(k,v)