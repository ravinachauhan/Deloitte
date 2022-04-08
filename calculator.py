'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Enter 1 for add")
print("Enter 2 for sub")
print("Enter 3 for mul")
print("Enter 4 for div")
choice=int(input("Enter choice"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
else:
    print(a/b)
    
