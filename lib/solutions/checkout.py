

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # to do: name these fields better

    promotions = {
        'single_item': {
            'A': [
                {
                    'multiplier': 3,
                    'amount': 130,
                },
                {
                    'multiplier': 5,
                    'amount': 200,
                }
            ],
            'B': [{
                'multiplier': 2,
                'amount': 45,
            }],
        },
        'bundle': {
            'E': {
                'multiplier': 2,
                'target_item': 'B'
            }
        }
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

    # apply bundle promotions first


    for item in basket:
        non_promo_number = basket[item]
        if item in promotions:
            multiplier = promotions[item]['multiplier']
            non_promo_number = basket[item] % multiplier
            amount += (basket[item] - non_promo_number)/multiplier*promotions[item]['amount']
        
        amount += non_promo_number*prices[item]

    return amount

def _apply_bundle_promos(basket):

