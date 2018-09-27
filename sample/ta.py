lis = [4,5,8,7,9,22]
"""
val = sorted(lis,reverse=True)
print val
lis.sort(reverse=True)
print lis
"""
lis.reverse()
print lis

lis = [4,5,8,7,9,22]
print(list(reversed(lis)))

lis = "python"
print(list(reversed(lis)))

re = [1,2,3,4]
re.remove(3)
print re

re = [3,4,5,6]
del re[3]
print re
