def discount_price(discount):
    def calculate_price(price):
        price=price*(1-discount)
        return price
    return calculate_price  