print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection")
total = 0
order_list = []
def print_menu():
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")
while True:
    print_menu()
    num = int(input("Enter your selection: "))

    if num == 1:
        print("You selected a Taco")
        total = total + 2.50
        order_list.append("Taco")

    elif num == 2:
        print("You selected a Burrito")
        total = total + 5.00
        order_list.append("Burrito")

    elif num == 3:
        print("You selected Nachos")
        total = total + 4.25
        order_list.append("Nachos")

    elif num == 4:
        print("You selected a Soft Drink")
        total = total + 1.50
        order_list.append("Soft Drink")

    elif num == 5:
        break

    else:
        print("Invalid selection. Please choose 1-5.")
print(f"You ordered {', '.join(order_list)}")
print(f"Your total is: ${total:.2f}")
