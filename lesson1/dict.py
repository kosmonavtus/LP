# 1 
example_dict = {"City": "Moscow", "Temperture": 20 }
print(example_dict['City'])
example_dict["Temperture"] = example_dict["Temperture"] - 5
print(example_dict)

# 2
print('country' in example_dict)
print(example_dict.get('country', "RU"))
example_dict['date'] = "27.05.2019"
print(example_dict)
print(len(example_dict))