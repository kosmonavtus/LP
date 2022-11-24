stock = [
        {'name': 'iphone12', 'Stock': 24, 'price': 653234, 'discount': 25 },
        {'name': 'iphone13', 'Stock': 10, 'price': 800000, 'discount':5 },
        {'name': 'Samsung', 'Stock': 5, 'price': 850000, 'discount': 11 }
]


def discounted(price, discount, max_discount=30, phone_name=' '):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError ("Price is to mach")
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)
    
for phone in stock:
    phone['price_final'] = discounted(phone['price'], phone['discount'], phone_name=phone['name'])
print(stock)


classes = [
        {'name': '3A', 'scores': [3,4,4,5,2]},
        {'name': '3B', 'scores': [5,5,3,2,2]},
        {'name': '3C', 'scores': [4,5,3,5,4]}
]

def count_avg(sttudents_scores):
    scores_sum = 0
    for score in sttudents_scores:
        scores_sum += score
    scores_avg = scores_sum / len(sttudents_scores)
    return scores_avg

for one_class in classes:
    class_score_avg = count_avg(one_class['scores'])
    print(f"AVG Score for claass {one_class['name']}: {class_score_avg}")

avg_scores_sum = 0
for one_class in classes:
    avg_scores_sum += count_avg(one_class['scores'])

    
school_avg = avg_scores_sum / len(classes)
school_avg_round =  round(school_avg, 2)
print(f"AVG Score for school: {school_avg_round}")