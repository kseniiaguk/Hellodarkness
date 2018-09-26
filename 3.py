#Не обращайте внимания на "3.py", это задание №1
def rotate(x):
    y=[0]*len(x)
    for i in range(0,len(x)):
        if i!=0:
            y[i]=x[i-1]
        else:
            y[i]=x[len(x)-1]
    return (y)
n=int(input())
a=[]
for i in range (0,n):
    a.append(int(input()))
c=rotate(a)
print(c)
