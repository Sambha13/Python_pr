num=int(input("Enter the number"))
fact=1
if num<0:
    print("Sorry,Factorial does not exit for negative number")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range (1,num+1):
        fact=fact*i
    print("The Factorial of number ",num,"is ",fact)
