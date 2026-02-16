# Function to determine letter grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Ask for student name
student_name = input("Enter student name: ")

# Ask for five grades (no loops)
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))

# Put grades into a list
grades = [grade1, grade2, grade3, grade4, grade5]

# Calculate average
average = sum(grades) / len(grades)

# Get letter grade using function
letter = get_letter_grade(average)

# Output
print("\n" + student_name)
print("\nAverage:", round(average, 1))
print("\nLetter Grade:", letter)
