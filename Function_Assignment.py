#Life is a function assigment
import math

#Area of circle
radius = int(input("Enter a radius: "))
pi = 3.14
def area_of_circle(pi, radius):
    return pi * radius * radius
print(f"{area_of_circle(pi, radius):.2f}")

#Taxes
money = int(input("Enter a money: "))
tax_rate = int(input("Enter tax rate: "))
tax_rate /= 100
def total_due(money, tax_rate):
    return money + (money * tax_rate)
print(f"{total_due(money, tax_rate):.2f}")

#Temperature
temp = int(input("Enter a temperature in fahrenheit: "))
def fahrenheit(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit(temp):.4f}")
