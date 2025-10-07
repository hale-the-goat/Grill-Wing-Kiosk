# =========================
# VIEW (Console Interface)
# =========================

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"
BOLD = "\033[1m"

def welcome_screen():
    print(f"{RED}🍗 Welcome to Grill Wing! Self-Service Kiosk! 💻🎉{RESET}")
    print(f"{YELLOW}🔥 Where every bite takes flight! 🔥{RESET}\n")

def show_dine_options():
    print(f"\n{BOLD}----- DINE IN OR TAKE OUT -----{RESET}")
    print(f"{CYAN}1.{RESET} Dine In")
    print(f"{CYAN}2.{RESET} Take Out")
    print(f"{RED}0.{RESET} Exit")

def show_categories(menu):
    print(f"\n{BOLD}----- SELECT CATEGORY -----{RESET}")
    for i, (category, _) in enumerate(menu, start=1):
        print(f"{CYAN}{i}.{RESET} {category}")
    print(f"{MAGENTA}C.{RESET} View Cart")
    print(f"{GREEN}CONFIRM.{RESET} Confirm Order")
    print(f"{RED}0.{RESET} Exit")
