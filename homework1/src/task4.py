def calculate_discount(price, discount):
    if type(price) != int and type(price) != float:
        return "error must be number"
    elif price < 0:
        return "price must be positive"
    elif discount < 0:
        return "discount must be positive"
    elif discount > 100:
        return "discount must be less than 100"
    else:
        discount_amount = price * (discount/100)
        final_price = price - discount_amount
        rounded_price = (round(final_price, 2))
        return rounded_price


#price = float(input("Enter your price:"))
#discount = float(input("Enter your discount:"))
#print(calculate_discount(price, discount))
