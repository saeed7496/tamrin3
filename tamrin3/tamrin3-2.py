
n=int(input('inter length of list: '))
lst=[] 

for i in range(n):
    a=float(input('enter number: '))
    lst.append(a)
    
if n ==1:print('list is sort')

for i in range(1,n):
    if lst[i]<lst[i-1]:
        print('list not sort')
        break
    elif i==n-1 :
        print('list is sort')
'''
n=int(input('inter length of list: '))
lst=[] 
lst2=[]
for i in range(n):
    a=float(input('enter number: '))
    lst.append(a)
    lst2.append(a)
if lst.sort()==lst2:
    print(lst,'is sort')
else:
    print(lst2,'is not sort')

'''





