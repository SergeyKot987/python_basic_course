from Homework7.function7.card_func import *
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


print(your_name.upper())
print(number_card)
print(what_bank(number_card))
print(exp_date)
print(cvv_code)

with open('homework.txt', 'w') as doc:
    doc.write(f"Your name - {your_name.upper()}, number card - {number_card}, expiration date - {exp_date}, cvv code - {cvv_code}")

with open('homework.txt', 'r') as doc:
    r = doc.read()
    print(r)
