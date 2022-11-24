some_list = ['Vasya', 'Masha', 'Petyaaa', 'Valera', 'Sasha', 'Dasha']

def find_person(some_list):
    while True:
        name = some_list.pop()
        if name == 'Valera':
            return print(f'{name} was found')

#find_person(some_list)


def ask_user(answer = None):
    while True:
        value = input("Как дела?\n")
        if value == 'хорошо':
            return False
        elif value != 'пока':
            get_answer(value)
        else:
            break

def get_answer(input):
    if input != "пока":
        print(f'{input} Это вопрос?')
        return True


if __name__ == '__main__':
    find_person(some_list)
    ask_user()
