def dodawanie(a, b):
	return a + b
def get_info():
	return "To jest program stworzony przez: Asia"	
try:	
	a = int(input('Podaj pierwszą liczbę: '))	
	b = int(input('Podaj drugą liczbę: '))
	print(dodawanie(a,b))
except ValueError as ve:
	print("Wprowadzono błędne dane, kończe działanie..."")

print(get_info())
input()