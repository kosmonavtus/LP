def get_summ(one: str, tow: str, delimiter = '&')-> str:
    result = str(one)+delimiter+str(tow)
    return result.upper()

if __name__ == '__main__':
    print(get_summ('Learn','python'))
