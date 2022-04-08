'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

words=input("Enter the words : ")
lst=[]
for i in words:
    if i.isdigit():
        lst.append(i)
print(lst)
        