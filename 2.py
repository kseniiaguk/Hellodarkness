def calc(x,y,z):
    if y=='+' or y=='-' or y=='*' or y=='/':
        if y=='+':
            return (int(x)+int(z))
        if y=='-':
            return (int(x)-int(z))
        if y=='*':
            return (int(x)*int(z))
        if y=='/':
            if z!=0:
                return (int(x)/int(z))
            else:
                return ('Нельзя делить на 0')
    else:
        return ('Неизвестная операция')
a,b,c=map(str,input().split())
x=calc(a,b,c)
print(x)
