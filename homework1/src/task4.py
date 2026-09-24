def calculate_discount(price, discount):
    try:
        if price < 0:
            raise ValueError("price must be > 0")
        elif discount < 0:
            raise ValueError("discount must be positive")
        elif discount > 100:
            raise ValueError("discount must be less than 100")
        else:
            discount_amount = price * (discount/100)
            final_price = price - discount_amount
            rounded_price = (round(final_price, 2))
            return rounded_price
    except TypeError:
        raise TypeError("value must be a number")
