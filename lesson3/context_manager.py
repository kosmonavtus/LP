with open('lesson3/file.txt','r') as file:
    letters_len = 0
    word_len = 0
    exclamation_marcks = ' '
    for string in file:
        letters_len += (len(string))
        word_len += (len(string.split()))
        exclamation_marcks += string.replace('.', '!')
    print(f'Всего букв в файле {file.name}: {letters_len}')
    print(f'Всего слов в файле {file.name}: {word_len}')

with open('lesson3/referat2.txt', 'w') as write_file:
    write_file.write(exclamation_marcks)
    





