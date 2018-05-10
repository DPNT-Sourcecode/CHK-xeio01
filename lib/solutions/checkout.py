# -*- coding: utf-8 -*-

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}

# make a frontend interface for the people responsible for pricing pls

PROMOTIONS = {
    'single_item': {
        # ordered list from highest multipler to lowest
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)],
    },
    'bundle': {
        'E': {
            'multiplier': 2,
            'target_item': 'B'
        },
        'F': {
            'multiplier': 2,
            'target_item': 'F'
        },
        'N': {
            'multiplier': 3,
            'target_item': 'M',
        },
        'R': {
            'multiplier': 3,
            'target_item': 'Q',
        },
        'U': {
            'multiplier': 3,
            'target_item': 'U',
        },
    }
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    basket = { item: 0 for item in PRICES }

    for char in skus:
        if char not in PRICES:
            return -1
        basket[char] += 1 

    # apply bundle promotions first
    # this removes items that will be free from the basket,
    # since currently bundles don't change the item price
    remaining_basket = _apply_bundle_promos(basket)

    # theres no item with both this promo and the ones above, so all good
    amount, remaining_basket = _apply_weird_new_promo(remaining_basket)
    print amount, remaining_basket
    # theres no item with both this promo and the ones above, so all good
    new_amount, remaining_basket = _apply_single_item_promos(remaining_basket)
    amount += new_amount
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

def _apply_weird_new_promo(basket):
    # buy any 3 of (S,T,X,Y,Z) for 45 
    # there will be no new requirements coming in because this is the last part of the test
    
    # soooo
    # Zs are more expensive and we like our customers so group them first
    # S, T and Y are all the same price
    # then Xs
    # 
    # ZSYXXXZZ
    pass