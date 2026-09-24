def calculate_discount(price, discount):
    discount_amount = price * (discount/100)
    final_price = price - discount_amount
    rounded_price = (round(final_price, 2))
    return rounded_price


#price = float(input("Enter your price: "))
#discount = float(input("Enter your discount: "))

#print(calculate_discount(30, 15.25))
