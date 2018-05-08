

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

    # assuming it's 4A not AAAA

    basket = {}

    for i in range(len(skus)):
        if skus[i]
        basket[skus[i+1]] = skus[i]
    
    amount = 0

    return -1
