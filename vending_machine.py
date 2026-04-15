class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self, number):
        print(f"{number}. {self.name} - ${self.price:.2f}")


class VendingMachine:
    def __init__(self):
        self.beverages = [
            Beverage("Water", 1.25),
            Beverage("Coke", 1.75),
            Beverage("Sprite", 1.75),
            Beverage("Orange Juice", 2.00),
            Beverage("Coffee", 1.50),
            Beverage("Tea", 1.50)
        ]

    def show_menu(self):
        print("\n===== VENDING MACHINE =====")
        for i, beverage in enumerate(self.beverages, start=1):
            beverage.display_info(i)
        print("===========================\n")

    def vend(self):
        while True:
            self.show_menu()

            choice = input("Select a beverage by entering 1-6: ")

            if not choice.isdigit():
                print("Invalid input. Please enter a number from 1 to 6.")
                continue

            choice = int(choice)

            if choice < 1 or choice > 6:
                print("That selection is not available. Please choose again.")
                continue

            selected_beverage = self.beverages[choice - 1]
            print(f"You selected: {selected_beverage.name}")
            print(f"Price: ${selected_beverage.price:.2f}")

            total_money = 0.0

            while total_money < selected_beverage.price:
                try:
                    money = float(input("Insert money: $"))
                    if money <= 0:
                        print("Please insert a valid amount of money.")
                        continue
                    total_money += money

                    if total_money < selected_beverage.price:
                        remaining = selected_beverage.price - total_money
                        print(f"Not enough money. Please add ${remaining:.2f} more.")
                except ValueError:
                    print("Invalid amount. Please enter a number.")

            change = total_money - selected_beverage.price

            print(f"\nVending {selected_beverage.name}...")
            if change > 0:
                print(f"Your change is: ${change:.2f}")
            print("Thank you for using the vending machine!\n")


# Main program
machine = VendingMachine()
machine.vend()