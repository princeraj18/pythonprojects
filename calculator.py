a=int(input("enter first no:"))
b=int(input("enter second no:"))
op=input("enter operator like:+,-,/,* ")
if(op=="+"):
    print(a+b)
elif(op=="-"):
    print(a-b)
elif(op=="*"):
    print(a*b)
elif(op=="/"):
    print(int(a/b))
else:
    print("invalid")
