mystr=input("Enter the string")
i=int(input("Enter the index of character to be remove:"))
resstr=" "
for index in range(len(mystr)):
    if index!=i:
        resstr=resstr+mystr[index]
print("Enter String:"+mystr)
print("String formed by removing i'th character:"+resstr)
