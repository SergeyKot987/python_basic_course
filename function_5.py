def card_func():
    while True:
        c = input("Enter yout number card\n")
        card_list = c.split(" ")
        if len(card_list) != 4:
            print("card number incorrect")
            continue
        has_error = False
        for el in card_list:
            if len(el) != 4:
                has_error = True
                break
        if has_error:
            print("incorrect")
            continue
        break
    

    if card_list[0] == "5167":
        print("You use Privatbank credit card")
    elif card_list[0] == "5375":
        print("You use MonoBank credit card")
    else:
        print("You use unknown ")
      return c  

def date_func():
    while True:
        date = input("Enter your date\n ")
        date_list = date.split("/")
        if len(date_list) != 2:
            print("incorrect")
            continue
        date_error = False
        for i in date_list:
            if len(i) != 2:
                date_error = True
                break
            if date_error:
                continue
        break
    return date        

def cvv_func():
    while True:
        cvv = input('Enter the CVV code: \n')
        if len(cvv) == 3:
            try:
                cvv = int(cvv)
                break
            except ValueError:
                print('Enter 3 numbers ')
        else:
            print('Enter 3 numbers ')
    return cvv            
            
