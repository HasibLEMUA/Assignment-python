number=int(input("enter your number"))
sum=0
while number>0:
    lastdigit= number%10
    sum+=lastdigit
    number//=10
print(sum)

    