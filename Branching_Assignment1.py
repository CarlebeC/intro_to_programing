# Branching Assignment

hours = int(input("Enter the KW hours used: "))
if hours <= 1000:
    total_cents = hours * 7.633
else:
# This is the "over 1000" part
    overage = hours - 1000
    total_cents = (1000 * 7.633) + (overage * 9.259)
# Now converting the cents to dollars
amount_owed = total_cents / 100

print("Amount owed is $", amount_owed)