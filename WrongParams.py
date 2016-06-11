from math import sqrt
def WParams(N):
    for i in range(int(sqrt(N)+1),N):
        param=sqrt(pow(i,2)-N)
        if param%1 == 0:
            break
    return i+param,i-param

print("введите для близких простых числа")
p=int(input("первое:"))
q=int(input("второе:"))
p1,q2=WParams(p*q)
print("Ваши параметры:",p1,q2)
