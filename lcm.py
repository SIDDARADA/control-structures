n1=int(input())
n2=int(input())
for i in range(1,n1*n2+1):
    if i%n1 == 0 and i%n2==0:
        print(f"LCM of {n1} and {n2} is {i}")
        break
