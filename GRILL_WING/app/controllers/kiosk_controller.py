from app.models.menu_model import menu
from app.models.cart_model import cart, add_to_cart, view_cart, clear_cart, checkout_details
from app.views.console_view import *

# Ensure checkout_details is initialized if empty
if not checkout_details:
    checkout_details.append("")

def start_kiosk():
    welcome_screen()
    show_dine_options()

    # Choose dine option
    while True:
        dine = input(f"\n➡ {YELLOW}Select option: {RESET}")
        if dine == "0":
            print(f"{MAGENTA}👋 Thank you for visiting Grill Wing!{RESET}")
            return
        elif dine == "1":
            checkout_details[0] = "Dine In"
            break
        elif dine == "2":
            checkout_details[0] = "Take Out"
            break
        else:
            print(f"{RED}❌ Invalid input, try again.{RESET}")

    # Category selection loop
    while True:
        show_categories(menu)
        selection = input(f"\n📂 Select a category: ").upper()

        if selection == "0":
            print(f"{MAGENTA}\n👋 Thank you for visiting Grill Wing! Come again soon!{RESET}")
            break
        elif selection == "C":
            show_cart()
            continue
        elif selection == "CONFIRM":
            confirm_order()
            break
        elif selection.isdigit() and 1 <= int(selection) <= len(menu):
            category_name, items = menu[int(selection) - 1]
            print(f"\n{BOLD}{category_name}{RESET}")
            for code, name, price in items:
                print(f"{CYAN}{code}{RESET} - {name} - ₱{YELLOW}{price:.2f}{RESET}")

            # Loop for valid item code
            while True:
                item_code = input("\nEnter item code (0 to go back): ").upper()

                if item_code == "0":
                    break  # Go back to category selection

                matched_item = next((i for i in items if i[0] == item_code), None)

                if matched_item:
                    # Loop for valid quantity
                    while True:
                        try:
                            qty = int(input(f"Enter quantity for {matched_item[1]}: "))
                            if qty > 0:
                                add_to_cart(*matched_item, qty)
                                print(f"{GREEN}✅ Added {qty}x {matched_item[1]} to cart!{RESET}")
                                input(f"➡ Press {CYAN}Enter{RESET} to continue...\n")
                                break  # Exit quantity loop
                            else:
                                print(f"{RED}❌ Quantity must be positive.{RESET}")
                                input(f"➡ Press {CYAN}Enter{RESET} to continue...\n")
                        except ValueError:
                            print(f"{RED}❌ Invalid quantity. Please enter a number.{RESET}")
                            input(f"➡ Press {CYAN}Enter{RESET} to continue...")
                    break  # Exit item code loop after successful add
                else:
                    print(f"{RED}❌ Invalid item code. Please try again.{RESET}")
                    input(f"➡ Press {CYAN}Enter{RESET} to continue...\n")
        else:
            print(f"{RED}❌ Invalid selection. Try again.{RESET}")
            input(f"➡ Press {CYAN}Enter{RESET} to continue...\n")


def show_cart():
    items, total = view_cart()
    print(f"\n{BOLD}----- 🛒 YOUR CART -----{RESET}")
    if not items:
        print(f"{YELLOW}🛒 Your cart is empty!{RESET}")
        input(f"\n➡ Press {CYAN}Enter{RESET} to go back...")
    else:
        for code, name, price, qty in items:
            print(f"{GREEN}{qty}x{RESET} {name} - ₱{YELLOW}{price * qty:.2f}{RESET}")
        print(f"\n{BOLD}Total: ₱{total:.2f}{RESET}")
        input(f"\n➡ Press {CYAN}Enter{RESET} to go back...")


def confirm_order():
    items, total = view_cart()
    if not items:
        print(f"{YELLOW}🛒 Your cart is empty! Add something first.{RESET}")
        input(f"\n➡ Press {CYAN}Enter{RESET} to go back...")
        return

    print(f"\n{BOLD}----- CHECKOUT -----{RESET}")
    for code, name, price, qty in items:
        print(f"{GREEN}{qty}x{RESET} {name} - ₱{YELLOW}{price * qty:.2f}{RESET}")
    
    print(f"\n{BOLD}Type of Order:{RESET} {CYAN}{checkout_details[0]}{RESET}")
    print(f"{BOLD}Total Amount:{RESET} ₱{YELLOW}{total:.2f}{RESET}")
    print(f"{GREEN}✅ Thank you for ordering at Grill Wing! 🍗 Enjoy your meal!{RESET}")
    
    clear_cart()
