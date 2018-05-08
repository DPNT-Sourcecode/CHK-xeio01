PRICES = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }

PROMOTIONS = {
    'single_item': {
        # ordered list from highest multipler to lowest
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
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
        if char not in PRICES:
            return -1
        basket[char] += 1 

    # apply bundle promotions first
    # this removes items that will be free from the basket,
    # since currently bundles don't change the item price
    remaining_basket = _apply_bundle_promos(basket)

    amount, remaining_basket = _apply_single_item_promos(remaining_basket)

    for item in remaining_basket:
        amount += remaining_basket[item]

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

            basket[target] = (
                0 
                if target_items_to_remove < 0 else
                target_items_to_remove
            )
            return basket
            
    return basket

def _apply_single_item_promos(basket):
    amount = 0
    for item in basket:
        if item in PROMOTIONS['single_item']:
            for promo in PROMOTIONS['single_item'][item]:
                multiplier = promo[0]
                non_promo_number = basket[item] % multiplier
                number_to_apply_promo = (basket[item] - non_promo_number)/multiplier
                amount += number_to_apply_promo*promo[1]
                items_left = basket[item] - number_to_apply_promo

                basket[item] = 0 if items_left < 0 else items_left
    return amount, basket