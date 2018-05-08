PRICES = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }

PROMOTIONS = {
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


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

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
    amount, remaining_basket = _apply_bundle_promos(basket)

    for item in basket:
        non_promo_number = basket[item]
        if item in promotions:
            multiplier = promotions[item]['multiplier']
            non_promo_number = basket[item] % multiplier
            amount += (basket[item] - non_promo_number)/multiplier*promotions[item]['amount']
        
        amount += non_promo_number*prices[item]

    return amount

def _apply_bundle_promos(basket):
    bundled_items = PROMOTIONS['bundle']

    for sku in basket:
        if sku in bundled_items:
            target = PROMOTIONS['bundle'][sku]['target_item']
            multiplier = PROMOTIONS['bundle'][sku]['multiplier']
            number_bundled_items = basket[sku]
            number_target_items = basket[target]
            target_items_to_remove = number_target_items - number_bundled_items/multiplier

            basket
            
    return 0, basket