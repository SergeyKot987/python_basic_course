from Homework6.function import *
while True:
    your_name = input("Enter your Name and Surname:\n")
    if check_your_name(your_name) == True:
        break

while True:
    number_card = input("Enter your card number (xxxx xxxx xxxx xxxx):\n")
    if check_credit_card(number_card) == True:
        break

what_bank(number_card)

year = 18
while True:
    exp_date = input("Enter expiration date:\n")
    if check_exp_date(exp_date, year) == True:
        break


while True:
    cvv_code = input("Enter your CVV code:\n")
    if check_cvv_code(cvv_code) == True:
        break

print("Your credit card information:\n")
print(your_name.upper())
print(number_card)
print(exp_date)
print(cvv_code)