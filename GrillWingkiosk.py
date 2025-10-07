# =========================
# ANSI COLOR CODES
# =========================
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"
BOLD = "\033[1m"

print(f"{RED}🍗 Welcome to Grill Wing! Self-Service Kiosk! 💻🎉{RESET}")
print(f"{YELLOW}🔥 Where every bite takes flight! 🔥{RESET}\n")

# =========================
# MENU ITEMS
# =========================
menu = [
    ("🍗 Favourites", [
        ("F1", "Double Drumstick Meal", 149.00),
        ("F2", "Solo Wing Rice Bowl", 99.00),
        ("F3", "Spicy Wing Burger", 129.00),
        ("F4", "Party Bucket (8 pcs)", 599.00),
        ("F5", "Wing Sampler Box", 249.00),
        ("F6", "Crispy Duo Combo", 189.00),
    ]),

    ("🍔 Burgers & Sandwiches", [
        ("B1", "Classic Wing Burger", 119.00),
        ("B2", "Spicy Blaze Burger", 139.00),
        ("B3", "Grilled Chick’n Melt", 149.00),
        ("B4", "Crispy Snackwich", 109.00),
    ]),

    ("🍟 Sides & Snacks", [
        ("S1", "Creamy Mash", 45.00),
        ("S2", "Cheesy Mac Mix", 49.00),
        ("S3", "Fresh Slaw Cup", 39.00),
        ("S4", "Crispy Fries", 55.00),
        ("S5", "Garlic Butter Corn", 49.00),
        ("S6", "Spicy Potato Wedges", 59.00),
        ("S7", "Onion Rings", 65.00),
    ]),

    ("🥤 Drinks & Desserts", [
        ("D1", "Classic Cola Float", 69.00),
        ("D2", "Iced Choco Frappe", 79.00),
        ("D3", "Chill Lemon Soda", 49.00),
        ("D4", "Vanilla Ice Swirl", 59.00),
        ("D5", "Strawberry Sundae", 69.00),
        ("D6", "Mango Cream Shake", 89.00),
        ("D7", "Cookies & Cream Blizzard", 99.00),
    ]),

    ("🍚 Rice Bowls", [
        ("R1", "Honey Glaze Bowl", 119.00),
        ("R2", "Fiery Garlic Bowl", 129.00),
        ("R3", "Creamy Wing Bowl", 109.00),
        ("R4", "Smoky Teriyaki Bowl", 139.00),
        ("R5", "Butter Soy Bowl", 125.00),
    ]),

    ("👑 Family & Group Meals", [
        ("G1", "Family Feast (4 pax)", 499.00),
        ("G2", "Barkada Bucket (6 pcs)", 399.00),
        ("G3", "Grill Wing Super Meal", 599.00),
        ("G4", "Celebration Feast", 799.00),
        ("G5", "Mega Party Platter", 999.00),
    ]),
]

cart = []
checkout_details = []

# =========================
# DINE-IN OR TAKE-OUT
# =========================
print(f"\n{BOLD}----- DINE IN OR TAKE OUT -----{RESET}")
print(f"{CYAN}1.{RESET} Dine In")
print(f"{CYAN}2.{RESET} Take Out")
print(f"{RED}0.{RESET} Exit")

while True:
    selection1 = input(f"\n➡ {YELLOW}Dine In or Take Out? {RESET}")
    if selection1 == "0":
        print(f"{MAGENTA}👋 Thank you for visiting Grill Wing! Come again soon!{RESET}")
        exit()
    elif selection1 == "1":
        checkout_details.append("Dine In")
        break
    elif selection1 == "2":
        checkout_details.append("Take Out")
        break
    else:
        print(f"{RED}❌ Invalid input, please choose again.{RESET}")

# =========================
# VIEW CART FUNCTION
# =========================
def view_cart():
    print(f"\n{BOLD}----- 🛒 YOUR CART -----{RESET}")
    if not cart:
        print(f"{YELLOW}🛒 Your cart is empty! Please add something first.{RESET}")
        input(f"\n➡ Press {CYAN}Enter{RESET} to continue...")
        return
    total = 0
    for code, name, price, qty in cart:
        subtotal = price * qty
        total += subtotal
        print(f"{GREEN}{qty}x{RESET} {name} - ₱{YELLOW}{subtotal:.2f}{RESET}")
    print(f"\n{BOLD}Total so far: ₱{total:.2f}{RESET}")
    input(f"\n➡ Press {CYAN}Enter{RESET} to go back to menu...")

# =========================
# SHOW ITEMS FUNCTION
# =========================
def show_items(category_name, items):
    while True:
        print(f"\n{BOLD}{category_name}{RESET}")
        for code, name, price in items:
            print(f"{CYAN}{code}{RESET} - {name} - ₱{YELLOW}{price:.2f}{RESET}")
        print(f"{RED}0.{RESET} Go Back")

        choice = input(f"\nEnter item code to add to cart (or 0 to go back): ").upper()
        if choice == "0":
            break

        for code, name, price in items:
            if choice == code:
                qty = int(input(f"How many {name} would you like? "))
                cart.append((code, name, price, qty))
                print(f"\n{GREEN}✅ {qty} x {name} added to cart!{RESET}")
                input(f"\n➡ Press {CYAN}Enter{RESET} to continue...")
                return
        else:
            print(f"{RED}❌ Invalid code. Try again.{RESET}")
            input(f"\n➡ Press {CYAN}Enter{RESET} to continue...")
            return

# =========================
# CATEGORY SELECTION
# =========================
while True:
    print(f"\n{BOLD}----- SELECT CATEGORY -----{RESET}")
    for i, (category, _) in enumerate(menu, start=1):
        print(f"{CYAN}{i}.{RESET} {category}")
    print(f"{MAGENTA}C.{RESET} View Cart")
    print(f"{GREEN}CONFIRM.{RESET} Confirm Order")
    print(f"{RED}0.{RESET} Exit")

    selection2 = input(f"\n📂 Select an option: ").upper()

    if selection2 == "0":
        print(f"{MAGENTA}\n👋 Thank you for visiting Grill Wing! Come again soon!{RESET}")
        break
    elif selection2 == "C":
        view_cart() # executes def view_cart()
    elif selection2 == "CONFIRM":
        if not cart:
            print(f"{YELLOW}🛒 Your cart is empty! Please add something first.{RESET}")
            input(f"\n➡ Press {CYAN}Enter{RESET} to continue...")
            continue
        print(f"\n{BOLD}----- CHECKOUT -----{RESET}")
        total = 0
        for code, name, price, qty in cart:
            subtotal = price * qty
            total += subtotal
            print(f"{GREEN}{qty}x{RESET} {name} - ₱{YELLOW}{subtotal:.2f}{RESET}")

        print(f"\nType of Order: {CYAN}{checkout_details[0]}{RESET}")
        print(f"{BOLD}Total Amount: ₱{total:.2f}{RESET}")
        print(f"\n{GREEN}✅ Thank you for ordering at Grill Wing! 🍗 Enjoy your meal!{RESET}\n")
        break
    elif selection2.isdigit() and 1 <= int(selection2) <= len(menu): # converts the input in selection2 to an integer
        category_name, items = menu[int(selection2) - 1]
        show_items(category_name, items) # executes def show_items(category name and items inside the category selected)
    else:
        print(f"{RED}❌ Invalid choice, please try again.{RESET}")
