def Repeat(N,e,y):
    y1=y
    while 1:
        y2=y1
        y1=pow(y1,e,N)
        if y1 == y:
            return y2
N=int(input("Модуль:"))
e=int(input("открытый ключ:"))
y=int(input("зашифрованное сообщение:"))
c=Repeat(N,e,y)
print("исходное сообщение:"+str(c))

print("проверка:",c,"^",e,"(mod",N,")=",pow(c,e,N))
