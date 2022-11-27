from collections import Counter

example_list = ['Iphone','Samsung','LG','Prosto_phone','Iphone','Iphone']

count = Counter(example_list)
print(count)


text = "какойто там текст для примера".lower().replace(" ","")

print(Counter(text))