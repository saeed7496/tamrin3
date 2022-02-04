
import random
lst=[]
n=int(input('inter length: '))
while len(lst) < n:
    x=random.randint(0,n)
    if x not in lst:
        lst.append(x)
    elif x in lst:continue
print(lst)
















