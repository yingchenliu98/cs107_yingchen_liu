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
        nonlocal balance 
        balance = balance - withdrawal_amount  
        if withdrawal_amount > balance:
            raise Exception("Sorry, your account doesn't have enough money.")    
        
        return balance
        
    return withdrawal

# demo
init_balance = 1000
withdrawal_amount = 500
new_withdrawal_amount = 200
print("Initial balance: ${:}".format(init_balance))
wd = make_withdrawal(init_balance)
print("Balance after the first withdrawal of amount ${} = $".format(withdrawal_amount), wd(withdrawal_amount))
print("Balance after the second withdrawal of amount ${} = $".format(new_withdrawal_amount),wd(new_withdrawal_amount))

