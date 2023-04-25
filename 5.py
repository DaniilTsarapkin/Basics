chislo = float(input("Введите число: "))
i =1
while i<=chislo:
    if chislo%i==0:
        print(i)
    i+=1

number = int(input("Введите число: "))
for i in range (1,number+1):
    if number%i==0:
        print(i)  

for j in range (60,131,10):
    print(j,j*0.6214)

number1 = int(input("Введите число: "))
i =1
while i**2<= number1:
    print(i**2)
    i+=1

Ar = list(map(int,input("Введите элементы массива: ").split()))
m =0
for i in range(len(Ar)):
    if m <= Ar[i]:
        m = i 
print(i +1)


h = 1
Ar1 =[]
while h!=0:
    h = int(input("Введите элемент последовательности: "))
    if h%2==0 and h !=0:
        Ar1.append(h)
print(*Ar1)

def wood(n):
    while n !=0:        
        print("    *    ")
        print("   ***   ")
        print("  *****  ")
        print(" ******* ")
        print("    |    ")
        n-=1
n = int(input("Введите количество елочек: "))
print(wood(n))

n,m = map(int,input().split())
A = [[(i+j+1)%2 for j in range(m)] for i in range(n)]
for g in A:
    print(*g)

n,m = map(int,input().split())
f = 0
B = [[j*m + i +1  for i in range(m)] for j in range(n)]
for w in B:
    print(*w)

n,m = map(int,input().split())
f = 0
B = [[i*n + j  for i in range(m)] for j in range(n)]
for w in B:
    print(*w)