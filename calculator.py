def dodawanie(a, b):
	return a + b
try:	
	a = int(input('Podaj pierwszą liczbę: '))	
	b = int(input('Podaj drugą liczbę: '))
	print(dodawanie(a,b))
except ValueError as ve:
	print("Wprowadzono błędne dane,", ve)
input()