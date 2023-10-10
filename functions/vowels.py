def count(val):
    v_count=0
    c_count=0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            v_count=v_count+1
        else:
            c_count=c_count+1
    print("vowel count is",v_count)
    print("consonant count is",c_count)
val=input("Enter a name")
count(val)
