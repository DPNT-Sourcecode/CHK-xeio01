PRICES = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
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
        },
        'F': {
            'multiplier': 2,
            'target_item': 'F'
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
        'E': 0,
        'F': 0,
    }

    for char in skus:
        if char not in PRICES:
            return -1
        basket[char] += 1 

    # apply bundle promotions first
    # this removes items that will be free from the basket,
    # since currently bundles don't change the item price
    remaining_basket = _apply_bundle_promos(basket)

    amount, remaining_basket = _apply_single_item_promos(basket)

    for item in remaining_basket:
        amount += remaining_basket[item]*PRICES[item]

    return amount

def _apply_bundle_promos(basket):
    bundled_items = PROMOTIONS['bundle']
    for sku in basket:
        if sku in bundled_items:
            target = PROMOTIONS['bundle'][sku]['target_item']
            multiplier = PROMOTIONS['bundle'][sku]['multiplier']
            # soz - i don't have time to think of something better right now, semi-hardcoding
            if sku != target:
                target_items_to_remove = basket[target] - basket[sku]/multiplier

                basket[target] = (
                    0 
                    if target_items_to_remove < 0 else
                    target_items_to_remove
                )
            else:
                leftover_fs = basket[sku]%(multiplier + 1)
                compressed_fs = basket[sku]/(multiplier+1)*multiplier
                basket[sku] = compressed_fs + leftover_fs
    return basket
            
    return basket

def _apply_single_item_promos(basket):
    amount = 0
    for item in basket:
        if item in PROMOTIONS['single_item']:
            for promo in PROMOTIONS['single_item'][item]:
                multiplier = promo[0]
                # how many items not to apply the promotion to
                non_promo_number = basket[item] % multiplier
                number_to_apply_promo = basket[item] - non_promo_number
                if number_to_apply_promo > 0:
                    amount += promo[1]*number_to_apply_promo/multiplier
                    items_left = basket[item] - number_to_apply_promo
                    basket[item] = 0 if items_left < 0 else items_left
    return amount, basket
