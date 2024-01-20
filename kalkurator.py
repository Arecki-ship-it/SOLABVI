#!/usr/bin/env python3

#Arecki
#666666666
#Beta1.0

def addition(a, b):
	return a + b
def subtract(a, b):
	return a - b
def multiply(a, b):
	return a * b
def divide(a, b):
	return a / b
def exponentiation(a, b):
	return a ** b
print("Elo wiesz co sie liczy? Wybierz dobrze!")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. **")
while True:
	choice = int(input("Chce: "))
	if choice <= 5:
		try:
			num1 = int(input("Pierwsza liczba: "))
			num2 = int(input("Druga liczba: "))
		except ValueError:
			print("Liczba!")
			continue

		if choice == 1:
			print(num1, "+", num2, "=", addition(num1, num2))
		elif choice == 2:
			print(num1, "-", num2, "=", subtract(num1, num2))
		elif choice == 3:
			print(num1, "*", num2, "=", multiply(num1, num2))
		elif choice == 4:
			print(num1, "/", num2, "=", divide(num1, num2))
		elif choice == 5:
			print(num1, "**", num2, "=", exponentiation(num1, num2))
		break
