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
        if withdrawal_amount > balance:
            raise Exception("Sorry, your account doesn't have enough money.")
        new_balance = balance - withdrawal_amount   
        return new_balance
    return withdrawal

# demo
init_balance = 1000
withdrawal_amount = 500
new_withdrawal_amount = 200
print("Initial balance: ${:}".format(init_balance))
wd = make_withdrawal(init_balance)
print("Balance after the first withdrawal of amount ${} = $".format(withdrawal_amount), wd(withdrawal_amount))
print("Balance after the second withdrawal of amount ${} = $".format(new_withdrawal_amount),wd(new_withdrawal_amount))


explaination= "Fail explaination: Becauce we created one withdrawal function 'wd' using 'init_balance'. "+\
    "Then every time we called 'wd', we will use the same inital balance instead of new balance returned by the previous wd in the inner function. " +\
    "The balance variable is bound in a block of the outer function, it is a local variable of that block unless declared as nonlocal or global. "+\
    "Each occurrence of a name in the program text refers to the binding of that name. "
print(explaination)