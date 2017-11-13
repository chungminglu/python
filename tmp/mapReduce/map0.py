def add(x):
    return x*x

res = map(add,range(1,7))
print(type(res))
for x in res:
    print(x)