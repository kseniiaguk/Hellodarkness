#это первый вариант, не смотрите его, пожалуйста...
def calc(x,y,z):
    if y=='+' or y=='-' or y=='*' or y=='/':
        if y=='+':
            return (x+z)
        if y=='-':
            return (x-z)
        if y=='*':
            return (x*z)
        if y=='/':
            try:
                return (x/z)
            except ZeroDivisionError:
                print ('Нельзя делить на 0')
    else:
        return ('Неизвестная операция')
a=str(input())
x1=str('')
y1=str('')
z1=str('')
k=0
for i in range(0,len(a)):
   if a[i].isdigit()==False and a[i]!='.' and k==0 and i!=0:
       k+=1
       x1+=a[0:i]
       y1+=a[i]
       if a[i+1]=='(' and a[i+2]=='-':
           z1+=a[i+2:len(a)-1]
       else:
           z1+=a[i+1:len(a)]
x2=float(x1)
y2=y1
z2=float(z1)
x=calc(x2,y2,z2)
print(x)
