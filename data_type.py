def have_fun(value: int, const: int = 10)-> int:
    if int(value) > 10 or int(value) < 1:
        raise 'i did told you no more than 10 and no less than 1'
    else:
        result = value+const
        return result

def what_is_y_name()-> str:
    user_name = input('What is you name? \n')
    return print(f'Hellow {user_name} how are you?')

def funy_print()-> None:
    try:
        print(int('2.5'))
    except Exception:
        print('Newer dont try to insert string into int')
    try:
        print(float('1'), '- python could lead string to the float type')
    except Exception:
        TypeError
    try:
        print(bool(1), '- is TRUE! ')
    except Exception:
        TypeError
    try:
        print(bool(' '), "I wouldn't write like that empty sting in bool")
    except Exception:
        TypeError
    try:
        print(bool(0), 'It is work! returned False')
    except Exception:
        TypeError
    return None
    

if __name__ == "__main__":
    value = int(input('write number betwen 1 and 10 \n'))
    print(have_fun(value))
    what_is_y_name()
    funy_print()