import re

def check_your_name(your_name):
    your_name_error = re.match(r'^[a-zA-Z]+\ [a-zA-Z]+$', your_name)
    if your_name_error:
        return True

def check_credit_card(number_card):
    card_error = re.match(r'(^[0-9]{4}\ [0-9]{4}\ [0-9]{4}\ [0-9]{4}$)', number_card)
    if card_error:
        return True

def what_bank(number_card):
    if number_card.startswith('5167'):
        print("You use PrivatBank card\n")
    elif number_card.startswith('5375'):
        print("You use Monobank credit card\n")
    else:
        print("You use credit card from unknown bank\n")

def check_exp_date(exp_date, year):
    exp_date_error = re.match(r'(^[0-9]{2}\/[0-9]{2}$)', exp_date)
    exp_date_list = exp_date.split('/')
    if exp_date_error and int(exp_date_list[1]) >= year and int(exp_date_list[0]) >= 1 and int(exp_date_list[0]) <= 12:
        return True

def check_cvv_code(cvv_code):
    cvv_code_error = re.match(r'^[0-9]{3}$', cvv_code)
    if cvv_code_error:
        return True