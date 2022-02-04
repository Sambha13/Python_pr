num1=int(input("Enter a first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third numeber:"))
def Maxi():
    if(num1>=num2) and (num1>=num3):
        max=num1
    elif(num2>=num1) and (num2>=num3):
        max=num2
    else:
        max=num3
    print("Largest number among the three is ",max)
Maxi()
