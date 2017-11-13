import time
s = time.clock()
for x in range(9999999):
    pass
e = time.clock()
print('耗時 : ',e-s)