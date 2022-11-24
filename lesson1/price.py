def format_price(price: int)-> str:
    result = str(f'Цена: {price} руб.')
    return result
    
if __name__ == "__main__":
    value = format_price(56.24)
    print(value)
