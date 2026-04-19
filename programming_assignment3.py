
#Programming assignment 3

FIRST_CLASS_ROWS = [1]
EMERGENCY_ROWS = [3, 4]
FIRST_CLASS_FEE = 50
ROWS = 5
SEATS_PER_ROW = 4
SEAT_LETTERS = ['A', 'B', 'C', 'D']


def create_seats():
    seats = {}
    for row in range(1, ROWS + 1):
        for letter in SEAT_LETTERS:
            seat_code = f"{row}{letter}"
            seats[seat_code] = False
    return seats


seats = create_seats()


def display_seats(seat_chart):
    print("\n--- DELTA SEATING CHART ---")
    print("X = Taken   O = Open")
    for row in range(1, ROWS + 1):
        row_display = []
        for letter in SEAT_LETTERS:
            seat_code = f"{row}{letter}"
            status = "X" if seat_chart[seat_code] else "O"
            row_display.append(f"{seat_code}:{status}")
        print("  ".join(row_display))

    print("\nFirst Class Rows:", FIRST_CLASS_ROWS, f"(${FIRST_CLASS_FEE} fee per seat)")
    print("Emergency Rows:", EMERGENCY_ROWS)
    print("Regular seats have no seat selection fee.")


def get_row_number(seat_code):
    return int(seat_code[:-1])


def valid_seat_format(seat_code):
    if len(seat_code) < 2:
        return False

    row_part = seat_code[:-1]
    seat_letter = seat_code[-1]

    if not row_part.isdigit():
        return False

    row_number = int(row_part)
    if row_number < 1 or row_number > ROWS:
        return False

    if seat_letter not in SEAT_LETTERS:
        return False

    return True


def emergency_confirmation(seat_code):
    row = get_row_number(seat_code)
    if row in EMERGENCY_ROWS:
        while True:
            answer = input(
                f"Seat {seat_code} is in an emergency row. "
                "Are you willing and able to assist in an emergency? (yes/no): "
            ).strip().lower()

            if answer == "yes":
                return True
            if answer == "no":
                print("You cannot select this emergency seat unless you accept responsibility.")
                return False
            print("Please enter yes or no.")

    return True


def purchase_seats(seat_chart):
    total_fee = 0
    seats_bought = []

    while True:
        display_seats(seat_chart)
        seat_choice = input("\nEnter the seat you want to buy (example: 2B): ").strip().upper()

        if not valid_seat_format(seat_choice):
            print("That is not a valid seat. Please choose a seat from 1A to 5D.")
            continue

        if seat_chart[seat_choice]:
            print("Sorry, that seat is already taken. Please choose another seat.")
            continue

        if not emergency_confirmation(seat_choice):
            continue

        seat_chart[seat_choice] = True
        seats_bought.append(seat_choice)

        row = get_row_number(seat_choice)
        if row in FIRST_CLASS_ROWS:
            total_fee += FIRST_CLASS_FEE
            print(f"Seat {seat_choice} purchased. First-class fee added: ${FIRST_CLASS_FEE}")
        else:
            print(f"Seat {seat_choice} purchased.")

        while True:
            more = input("Do you want to buy another seat? (yes/no): ").strip().lower()
            if more in ["yes", "no"]:
                break
            print("Please enter yes or no.")

        if more == "no":
            break

    print("\n--- PURCHASE SUMMARY ---")
    print("Seats purchased:", ", ".join(seats_bought))
    print(f"Seat selection fees due: ${total_fee}")
    print("Thank you for flying with Delta!")


def main():
    print("Welcome to come to Delta!")
    print("This plane has 20 seats total.")
    purchase_seats(seats)


main()
