from random import randint
from math import gcd
from math import fmod
from math import sqrt
def SqrtFunc(a,b,c):
    d=b*b-4*a*c
    if d<0 or fmod(sqrt(d),1)!=0:
        return -10,-10
    else:
        x1=(-b+sqrt(d))/(2*a)
        x2=(-b-sqrt(d))/(2*a)
        return x1,x2

"""p=int(input("p:"))
q=int(input("q:"))
N=p*q
f=(p-1)*(q-1)
while 1:
    e=randint(2,f)
    if gcd(e,f)==1:
        break
print('N:{0}\nf:{1}\ne:{2}'.format(N,f,e))
"""
p=12347
q=13001
N=p*q
e=60728973
mas=[]
n=N
E=e
for i in range(0,20):
    """Дробь может быть бесконечной"""
    mas.append(N//e)
    if N%e==0:
        break
    e1=e
    e=fmod(N,e)
    N=e1

P,Q=[],[]
P.append(0)
P.append(1)
Q.append(0)
Q.append(0)
Q.append(1)
for i in range(2,len(mas)+2):
    P.append(mas[i-2]*P[i-1]+P[i-2])
for i in range(2,len(mas)+1):
    Q.append(mas[i-1]*Q[i]+Q[i-1])
print(mas)
print(P)
print(Q)
for i in range(0,len(mas)):
    #print("P[",i,"+2]:",P[i+2],"Q[",i,"+2]:",Q[i+2])
    F=(E*P[i+2]-1)/Q[i+2]
    #print("F:",F)
    if fmod(F,1)!=0:
        #print("F not integer")
        continue
    x1,x2=SqrtFunc(1,-n+F-1,n)
    if x1==x2==-10:
        print("d<0")
        continue
    if fmod(x1,1)!=0 or fmod(x1,1)!=0:
        print("x1 or x2 not integer")
        continue
print(x1,x2)

