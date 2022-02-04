num=int(input("Enter the number"))
sum=0
temp=sum
order=len(str(num))
while temp>0:
    digit=temp % 10
    sum +=digit ** order
    temp //=10
if num==sum:
    print(num," is Armstrong")
else:
    print(num," is not Armstrong")
