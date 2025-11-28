import math_utils
def calculate_total_price(price , quantity):
    total = math_utils.multiply(price , quantity)
    return total
def apply_discount(total , discount):
    final_price = math_utils.subtract(total , discount )
    return final_price