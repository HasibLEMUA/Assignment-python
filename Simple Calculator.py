num1= float(input("enter 1st number"))
op=input("for addition press +,for  substraction press -,for divition press /, for multiplication press-")
num2= float(input("enter 2nd number"))
if op== "+":
    print(num1 ,"+",num2,"=",num1+num2)

elif op== "-":
    print(num1 ,"-",num2,"=",num1-num2)
elif op=="*":
    print(num1 ,"*",num2,"=",num1*num2)
elif op=="/":
    if num2 != 0:
        print( num1,"/",num2,"=", num1/num2)
    else:
        print("you cannot divided by zero")

