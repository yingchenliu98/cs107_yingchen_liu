#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:55:10 2020

@author: yingchenliu
"""
from Bank import BankAccount, BankUser, AccountType

def test_over_withdrawal(): #this test function should throw an Exception or Error 
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    try:
        user.withdraw(AccountType.SAVINGS, 1000); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption


def test_neg_amount():
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS,100);
    try:
        user.withdraw(AccountType.SAVINGS, -10);
    except Exception as e:
        print(e)


def test_duplicate_savings_account():
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    try:
        user.addAccount(AccountType.SAVINGS);
    except Exception as e:
        print(e)
        

def test_duplicate_checking_account():
    user = BankUser("Joe");
    user.addAccount(AccountType.CHECKING);
    try:
        user.addAccount(AccountType.CHECKING);
    except Exception as e:
        print(e)
        
def test_getBalance_no_account():
    user = BankUser("Joe");
    try:
        user.getBalance(AccountType.SAVINGS)
    except Exception as e:
        print(e)
                
        
def test_deposit_no_account():
    user = BankUser("Joe");
    try:
        user.deposit(AccountType.SAVINGS, 100)
    except Exception as e:
        print(e)
        
def test_withdraw_no_account():
    user = BankUser("Joe");
    try:
        user.withdraw(AccountType.SAVINGS, 100)
    except Exception as e:
        print(e)       
        
test_over_withdrawal();
test_neg_amount();
test_duplicate_savings_account();
test_duplicate_checking_account();
test_getBalance_no_account();
test_deposit_no_account();
test_withdraw_no_account();