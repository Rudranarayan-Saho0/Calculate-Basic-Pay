#Name = input("Employee Name: ")
BasicPay = float(input("Enter Your Basic Pay"))

if BasicPay > 20000:
    DA = 0.2*BasicPay
    TA = 0.1*BasicPay
    HRA = 0.05*BasicPay

elif BasicPay > 15000:
    DA = 0.2*BasicPay
    TA = 0.08*BasicPay
    HRA = 0.03*BasicPay

else:
    DA = 0.2*BasicPay
    TA = 0.05*BasicPay
    HRA = 0.02*BasicPay

print(f"Net salary On Basic {BasicPay} is {BasicPay+DA+TA+HRA}") 