cart = []
checkout_details = []

def add_to_cart(code, name, price, qty):
    cart.append((code, name, price, qty))

def view_cart():
    total = 0
    for code, name, price, qty in cart:
        total += price * qty
    return cart, total

def clear_cart():
    cart.clear()
    checkout_details.clear()
