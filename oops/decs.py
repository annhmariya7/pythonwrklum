def swap_nums(fn):    #define decorator
    def wrapper(n1,n2):        #inner fn
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper


@swap_nums            #calling decorator to reduce -ve values in operations
def sub(n1,n2):
    return n1-n2

@swap_nums
def div(n1,n2):
    return n1/n2

print(sub(5,10))
print(div(5,10))
