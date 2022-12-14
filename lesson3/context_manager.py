def read_and_write_some_files(inputfile: str, outputfile: str)-> None:
    with open('lesson3/file.txt','r') as file:
        letters_len = 0
        word_len = 0
        exclamation_marcks = ' '
        for string in file:
            letters_len += (len(string))
            word_len += (len(string.split()))
            exclamation_marcks += string.replace('.', '!')
        print(f'''Всего букв в файле {file.name}: {letters_len} \n 
                  Всего слов в файле {file.name}: {word_len}''')

    with open('lesson3/referat2.txt', 'w') as write_file:
        write_file.write(exclamation_marcks)

if __name__ == '__main__':
    inputfile = 'lesson3/file.txt'
    outputfile = 'lesson3/referat2.txt'
    read_and_write_some_files(inputfile,outputfile)



