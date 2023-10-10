#*args => used for passing many parameters

class Calculator():

    def add(self,*args):
        return sum(args)
    
obj=Calculator()
print(obj.add(637,677,5))


def product(*args):
    res=1
    for num in args:
        res*=num
    return res
print(product(2,4))


def max_word(*args):
        maximum_words= max(args,key=lambda w:len(w))
        return maximum_words

print(max_word("hello","goodmorning"))


# args => in tuple format