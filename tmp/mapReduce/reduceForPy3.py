from functools import reduce

def add(x,y):
    return x+y

print(reduce(add,range(1,7)))