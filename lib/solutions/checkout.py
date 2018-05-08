

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

    # assuming it's 4A not AAAA, and A comes in as 1A

    basket = {}

    for i in range(len(skus)):
        if skus[i] not in valid_skus:
            return -1
        if i%2 == 0:
            basket[skus[i+1]] = skus[i]
    
    amount = 0

    for item in basket:
        non_promo_number = 0
        if item in promotions:
            non_promo_number = basket[item] % promotions[item]['multiplier']
            amount += (basket[item] - non_promo_number)*promotions[item]['amount']
        
        amount += non_promo_number*prices[item]

    return amount
