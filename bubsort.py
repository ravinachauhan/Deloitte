'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

lst=[10,22,1,3,65,23]
for i in range(0,len(lst)-1):
    for j in range(0,len(lst)-i-1):
        if lst[j]>lst[j+1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print(lst)
