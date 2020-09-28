#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:58:00 2020

@author: yingchenliu
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:58:40 2020

@author: yingchenliu
"""
def make_withdrawal(balance): 
    def withdrawal(withdrawal_amount):
        try:
            balance = balance - withdrawal_amount  
        except Exception as error:
            print("Error message:", error)
            return "Failed"
        else:
            if balance < 0:
                raise Exception("Sorry, your account doesn't have enough money.")
            return balance
    return withdrawal

# demo
init_balance = 1200
withdrawal_amount = 600
new_withdrawal_amount = 500
wd = make_withdrawal(init_balance)
print("First withdrawal:" ,wd(withdrawal_amount))
print("Second withdrawal:", wd(new_withdrawal_amount))


explaination= "Fail explaination: A scope defines the visibility of a name within a block. 'balance' is a local variable defined in the make_withdraw block, its scope includes that block. "+\
    "When trying to update the balance after each function call, there will raise UnboundLocalError: local variable 'balance' referenced before assignment. " +\
    "This is because the current scope is a function scope, and the name refers to a local variabke that has not yet been bound to a value at the point where the name is used. " +\
    "At this time, we may need to use global or nonlocal statement to resolve the error."

print(explaination)