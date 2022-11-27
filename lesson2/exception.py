import random
import requests


def cut_cake(people):
    try:
        parts = 1 / people
        print(f'tock {parts}')
    except ZeroDivisionError:
        print('not divisible by zero, bitch')
    except TabError:
        print('Програма принимает на вход число сука')

def random_it():
    while True:
        part = random.randint(1,10)
        cut_cake(part)


def hellow_user():
    try:    
        while True:
            value = input("Как дела?\n")
            if value == 'хорошо':
                return False
            elif value == 'пока':
                return False
    except KeyboardInterrupt:
        print(" \n Пока юзерь ! ")


def discounted(price: float, 
              discount: float,
              max_discount: int = 30,
              phone_name=' '):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except(ValueError, TypeError):
        return print('Dont put it here!')    
    if max_discount >= 100:
        raise ValueError ("Price is to mach")
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)


def get_real_ip():
    url = 'http://ipify.org/'
    try:
        result = requests.get(url)
    except requests.ConnectTimeout:
        print('тут должен быть репит но мне лень')
    return print(result.content)

if __name__ == '__main__':
    #hellow_user()
    #discounted(10000.1, 10.5, 'gnusmus')
    get_real_ip()


