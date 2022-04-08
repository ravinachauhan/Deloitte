'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import re
passwords=input("enter your passwords").split(",")
accepted_passwords=[]
for i in passwords:
    if len(i) <6 or len(i)>12:
        continue
    elif not re.search("([a-z])+", i):
        continue
    elif not re.search("([A-Z])+", i):
        continue
    elif not re.search("([0-9])+", i):
        continue
    elif not re.search("([!@#$%^&])+", i):
        continue
    else:
        accepted_passwords.append(i)
print(accepted_passwords)
    
