#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:41:43 2020

@author: yingchenliu
"""
from enum import Enum
from sys import exit

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        """
        Parameters:
            owner is a string representing the name of the account owner
            accountType is one of the AccountType enums.
        """
        self.owner = owner
        self.accountType = AccountType(accountType)
        self.balance = 0.0
        
    def withdraw(self, amount):
        """
        Paramter:
            amount is an positive number.
        """
        if amount > self.balance:
            raise Exception("Sorry, your account doesn't have enough money.")
        elif amount < 0:
            raise Exception("Sorry, please enter a non-negative amount to withdraw.")
        else:
            self.balance -= amount
         
    
    def deposit(self, amount):
        """
        Paramter:
            amount is an positive number.
        """
        if amount < 0:
            raise Exception("Sorry, please enter a non-negative amount to deposit.")
        else:
            self.balance += amount

    def __str__(self):
        return ("The Owner of this account is {} "
                "and the Account Type is {}".format(self.owner, self.accountType.name))
    def __len__(self):
        return int(self.balance)


class BankUser():
    
    def __init__(self, owner):
        self.owner = owner
        self.checking = None
        self.savings = None


    def addAccount(self, accountType):
        
        if accountType == 1 or accountType == AccountType.SAVINGS:
            if self.savings != None:
                raise Exception("Sorry, one user can only have one saving account.")
            else:
                self.savings = BankAccount(self.owner, accountType)        
        
        elif accountType == 2 or accountType == AccountType.CHECKING:
            if self.checking != None:
                raise Exception("Sorry, one user can only have one checking account.")
            else:
                self.checking = BankAccount(self.owner, accountType)


    def getBalance(self, accountType):
        
        if accountType == 1 or accountType == AccountType.SAVINGS:
            if self.savings == None:
                raise Exception("This account doesn't exist. Please create a savings account first.")
                return "Failed"
            else:
                return len(self.savings)
        elif accountType == 2 or accountType == AccountType.CHECKING:
            if self.checking == None:
                raise Exception("This account doesn't exist. Please create a checking account first.")
                return "Failed"
            else:
                return len(self.checking)
        
        
    def deposit(self, accountType, amount):
        
        if accountType == 1 or accountType == AccountType.SAVINGS:
            if self.savings == None:
                raise Exception("This account doesn't exist. Please create a savings account first.")
                return "Failed"
            else:
                self.savings.deposit(amount)
        elif accountType == 2 or accountType == AccountType.CHECKING:
            if self.checking == None:
                raise Exception("This account doesn't exist. Please create a checking account first.")
                return "Failed"
            else:
                self.checking.deposit(amount)
        
        
    def withdraw(self, accountType, amount):
        
        if accountType == 1 or accountType == AccountType.SAVINGS:
            if self.savings == None:
                raise Exception("This account doesn't exist. Please create a savings account first.")
                return "Failed"
            else:
                self.savings.withdraw(amount)
        elif accountType == 2 or accountType == AccountType.CHECKING:
             if self.checking == None:
                raise Exception("This account doesn't exist. Please create a checking account first.")

             else:
                self.checking.withdraw(amount)


    def __str__(self):
        if self.checking!=None and self.savings!=None:
            return ("The user of account is {}. "
                    "This user has 1 {} account with a balance of {} and 1 {} account with a balance of {}.".format(self.owner,
                                                                  self.checking.accountType.name,
                                                                  self.getBalance(2),
                                                                  self.savings.accountType.name,
                                                                  self.getBalance(1)))
        elif self.checking!=None:
            return ("The user of account is {}. "
                    "This user has 1 {} account with a balance of {}.".format(self.owner, 
                                                                              self.checking.accountType.name,
                                                                              self.getBalance(2)))
        elif self.savings!=None:
            return ("The user of account is {}. "
                    "This user has 1 {} account with a balance of {}.".format(self.owner, 
                                                                              self.savings.accountType.name,
                                                                              self.getBalance(1)))                                                           
        else:
            return ("The user of the account is {}. There is no accounts under this user's name.".format(self.owner))


    
def ATMSession(bankUser):
    print("Hello, {}! Welcome to BMO, We care for you! \n".format(bankUser.owner))
    def Interface():
        while(True):
            try:
                ans = input("Enter Option:\n 1)Exit\n 2)Create Account\n 3)Check Balance\n 4)Deposit\n 5)Withdraw\nPlease enter an option:")
        
                if ans == '1':
                    print('\nThanks for banking with BMO. Hope to see you next time!')
                    exit()
                   
                elif ans == '2':
                    ans = input("Enter Option:\n 1)Checking\n 2)Savings\nPlease enter an option:")
                    if ans == '1':
                        try:
                            bankUser.addAccount(2)
                            print('\nSuccessfully created a new CHECKING account.')
                        except Exception as e:
                            print(e)
                    elif ans == '2':
                        try:
                            bankUser.addAccount(1)
                            print('\nSuccessfully created a new SAVING account.')
                        except Exception as e:
                            print(e)
                    else:
                        print("\nPlease enter a valid option.")
                   
                elif ans == '3':
                    ans = input("Enter Option:\n 1)Checking\n 2)Savings\nPlease enter an option:")
                    if ans == '1':
                        try: 
                            bal = bankUser.getBalance(2)
                            print('\nThe current balance of your CHECKING account is {}'.format(bal))
                        except Exception as e:
                            print(e)
                    elif ans == '2':
                        try:
                            bal = bankUser.getBalance(1)
                            print('\nThe current balance of your SAVING account is {}'.format(bal))
                        except Exception as e:
                            print(e)
                    else:
                        print("\nPlease enter a valid option.")
                        
                elif ans == '4':
                    ans = input("Enter Option:\n 1)Checking\n 2)Savings\nPlease enter an option:")
                    
                    if ans == '1':
                        amount = int(input("Enter Integer Amount, Cannot Be Negative:"))
                        try:
                            bankUser.deposit(2, amount)
                            print('\nSuccessfully deposited {} into your CHECKING account.'.format(amount))
                        except Exception as e:
                            print(e)
                    elif ans == '2':
                        amount = int(input("Enter Integer Amount, Cannot Be Negative:"))
                        try:
                            bankUser.deposit(1, amount)
                            print('\nSuccessfully deposited {} into your SAVINGS account.'.format(amount))
                        except Exception as e:
                            print(e)
                    else:
                        print("\nPlease enter a valid option.")
                        
                elif ans == '5':
                    ans = input("Enter Option:\n 1)Checking\n 2)Savings\nPlease enter an option:")
    
                    if ans == '1':
                        amount = int(input("Enter Integer Amount, Cannot Be Negative:"))
                        try:
                            bankUser.withdraw(2, amount)
                            print('\nSuccessfully withdrawn {} from your CHECKING account.'.format(amount))
                        except Exception as e:
                            print(e)
                    elif ans == '2':
                        amount = int(input("Enter Integer Amount, Cannot Be Negative:"))
                        try:
                            bankUser.withdraw(1, amount)
                            print('\nSuccessfully withdrawn {} from your SAVINGS account.'.format(amount))
                        except Exception as e:
                            print(e)
                    else:
                        print("\nPlease enter a valid option.")
                        
                else:
                    print("\nPlease enter a valid option.")
            except ValueError:
                print("Invalid input.")
    return Interface()
# demo
# user = BankUser("Joe")
# ATMSession(user)
























