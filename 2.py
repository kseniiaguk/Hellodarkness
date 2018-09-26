def calc(x,y,z):
    if y=='+' or y=='-' or y=='*' or y=='/':
        if y=='+':
            return (int(x)+int(z))
        if y=='-':
            return (int(x)-int(z))
        if y=='*':
            return (int(x)*int(z))
        if y=='/':
            try:
                return (int(x)/int(z))
            except ZeroDivisionError:
                print ('Нельзя делить на 0')
    else:
        return ('Неизвестная операция')
a=str(input())
x1=str('')
y1=str('')
z1=str('')
for i in range(0,len(a)):
   if a[i].isdigit()==False:
       x1+=a[0:i]
       y1+=a[i]
       z1+=a[i+1:len(a)]
x2=int(x1)
y2=y1
z2=int(z1)
x=calc(x2,y2,z2)
print(x)
