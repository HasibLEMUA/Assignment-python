H= float(input("enter your hight as a meter"))
w= float(input("enter your body weight as a kilogram"))
BMI= w/(H*H)
if BMI<18.5:
    print("underweight")
elif BMI >=18.5 and BMI<=24.9:
    print ("normal")
elif BMI>=25 and BMI<=29.9:
    print ("overweight")
elif BMI>=30:
    print("obese")