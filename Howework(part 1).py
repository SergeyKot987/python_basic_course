#1
adress = input("What street do you live?")
phone_number = input("What is your phone number?")
your_info = f"{adress}.{phone_number}"
print(your_info)
#2.1
ru_en = {"fish": "рыба", "car": "машина"}
try:
    value = ru_en["home"]
except KeyError:
    print("Такого слова нету")
#2.2
x = "qwert"
try:
    print(int(x))
except ValueError:
    print("Иди учись!")
#3.1
a = 22
b = 15
if not (a is b):
    print("Ura")
else:
    print("Error")
#3.2
c = 6
d = 20
if c > d and c >= d or c == d:
    print("c < d")
else:
    print("Vse verno")
#3.3


