rpass= 7890
i=0
while i<3:
    tpass=int(input("enter your password"))
    if tpass==rpass:
        print("welcome")
        break
    else:
        print("try again")
        i+=1
    if i==3:
     print("acount locked")


