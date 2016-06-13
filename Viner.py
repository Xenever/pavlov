from random import randint
from math import gcd
from math import fmod
from math import sqrt
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
#print(mas)
#print(P)
#print(Q)
for i in range(0,len(mas)):
    #print("P[",i,"+2]:",P[i+2],"Q[",i,"+2]:",Q[i+2])
    F=(E*P[i+2]-1)/Q[i+2]
    #print("F:",F)
    if fmod(F,1)!=0:
        continue
    Sum=n-F+1
    #print("Sum:",Sum)
    if Sum<0:
        continue
    Dif=sqrt(abs(pow(Sum,2)-4*n))
    #print("Dif:",Dif)
    if fmod(Dif,1)!=0:
        continue
    CalcP=(Sum-Dif)/2
    #print("CalcP:",CalcP)
    if CalcP<0 and fmod(CalcP,1)!=0:
        continue
    CalcQ=(Sum+Dif)/2
    #print("CalcQ:",CalcQ)
    if CalcQ<0 and fmod(CalcQ,1)!=0:
        continue
print(CalcP,CalcQ)
