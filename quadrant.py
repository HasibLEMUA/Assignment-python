x = float(input( "enter number for x)"))
y = float(input("input number for y"))
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x>0 and y<0:
    print("4th quardant")
elif y==0 and x>0 or x<0:
    print("lies on x exis")
elif x==0 and y<0 or y>0:
    print ("lies on y exis")
elif x==0 and y==0:
    print (" center ")

        