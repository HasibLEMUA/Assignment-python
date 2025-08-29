n=int(input("press your number"))
rn=0
while n>0:
    ld=n%10
    
    rn=rn*10+ld
    
    n//=10
    
print(rn)