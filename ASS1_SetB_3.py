num=int(input("Enter a number:"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
    if flag:
        print(num,"ïs not Prime Number:")
    else:
        print(num,"is a Prime Number:")