a=str(input())
k=0
for i in range (0,len(a)):
    if a[i]!=a[len(a)-1-i]:
        k+=1
        break
if k==0:
    print('Это палиндром')
else:
    print ('Это НЕ палиндром')
