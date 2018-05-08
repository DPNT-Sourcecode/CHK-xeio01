

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    valid_skus = ['A', 'B', 'C', 'D']

    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    promotions = {
        'A': {
            'multiplier': 3,
            'amount': 130,
        },
        'B': {
            'multiplier': 2,
            'amount': 45,
        },
    }

    # nope

    basket = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
    }

    for char in skus:
        if char not in valid_skus:
            return -1
        basket[char] += 1 
    
    amount = 0

    for item in basket:
        non_promo_number = 0
        if item in promotions:
            non_promo_number = basket[item] % promotions[item]['multiplier']
            amount += (basket[item] - non_promo_number)*promotions[item]['amount']
        
        amount += non_promo_number*prices[item]

    return amount
