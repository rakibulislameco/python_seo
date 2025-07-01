# price = 300
# discount = 0.10
#
# total_discount = price * discount
# total_price = price - total_discount
# print(total_price)

# def calculate_price(price,discount):
#     total_discount = price * discount
#     total_price = price - total_discount
#     return total_price
# item1 = calculate_price(300, .10)
# print(item1)

def calculate_price(price,discount=0.10):
    """
    :param pirce: any numbers
    :param discount: discount will be 0 to 1 e.g. 10% means 0.10
    :return: new price after discount
    """
    total_discount = price * discount
    total_price = price - total_discount
    return total_price

item_price = calculate_price(300)
item2_price = calculate_price(300,0.15)
# print(item_price)
print(item2_price)