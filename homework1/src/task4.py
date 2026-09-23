def calculate_discount(price, discount):
    discount_amount = price * (discount/100)
    final_price = price - discount_amount
    print(f"{final_price:.2f}")


price = float(input("Enter your price: "))
discount = float(input("Enter your discount: "))

calculate_discount(price, discount)
