# Mark Feehily
# Professor Santore
# COMP 490 - Homework 1
# 4/28/2022

def calculate_tax(price, tax_rate):
    Tax_total = price + (price * tax_rate)
    return Tax_total


total_price = float(input("Enter in the price of your items $"))
state = int(input("What state are you in?, Massachusetts[1] , Maine[2] , NewHampshire[3]"))

if state == 1:
    salesTax = .625
    total = calculate_tax(total_price, salesTax)
    print("Total with Massachusetts sales tax added", total)
if state == 2:
    salesTax = .55
    total = calculate_tax(total_price, salesTax)
    print("Total with Maine sales tax added", total)
if state == 3:
    salesTax = 0
    total = calculate_tax(total_price, salesTax)
    print("Total with NewHampshire sales tax added", total)


