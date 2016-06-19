#Extended Euclidean algorithm
def egcd(a, b):
    x, lastX = 0, 1
    y, lastY = 1, 0
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
    return (lastX, lastY)
#дробь по модулю(num-числитель,denom-знаменатель)
def Exponent(num,denom,mod):
    a,b=egcd(denom,mod)
    a=a*num
    while a>mod:
        a=a-mod
    return a
#WrongKeys
def WKey(y1,e1,y2,e2,N):
    a,b=egcd(e1,e2)

    if a<b:
        c=a
        a=b
        b=c
        c=y1
        y1=y2
        y2=c
    b=-b
    result=pow(int(int(pow(y1,a)//pow(y2,b))+Exponent(pow(y1,a)%pow(y2,b),pow(y2,b),N)),1,N)
    return result
"""
x=int(input("начальный текст:"))
e1=int(input("первый ключ:"))
e2=int(input("второй ключ:"))
N=int(input("модуль:"))
y1=pow(x,e1,N)
y2=pow(x,e2,N)
print(WKey(y1,e1,y2,e2,N))
"""


