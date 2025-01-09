# -*- coding: utf-8 -*-
"""
ISE224: HW1-10

@author: cxc1920
"""

shares_bought = int(input("How many shares he bought: "))
price_bought = float(input("Price per share he bought: "))
commission_bought = float(input("Commission rate of purchase: "))
shares_sold = int(input("How many shares he sold: "))
price_sold = float(input("Price per share he sold: "))
commission_sold = float(input("Commission rate of sale: "))

paid_for_stock = shares_bought * price_bought
commission_paid_bought = paid_for_stock * commission_bought

received_for_stock = shares_sold * price_sold
commission_paid_sold = received_for_stock * commission_sold

total_cost = paid_for_stock + commission_paid_bought
total_sale = received_for_stock - commission_paid_sold
total = total_sale - total_cost
print("He paid", paid_for_stock, "for the stock.")
print("He paid", commission_paid_bought, "to his broker when he bought this stock.")
print("He received", received_for_stock, "for the stock.")
print("He paid", commission_paid_sold, "to his broker when he sold this stock.")
print("He left", total)
