from __future__ import division

#List of constants
PI = 3.14159265359
ONE_EIGHTY_OVER_PI = 180 / PI
FIVE_OVER_NINE = 5/9
NINE_OVER_FIVE = 9/5


list_of_converstions = {
	'rd' : lambda number : number * ONE_EIGHTY_OVER_PI,
	'dr' : lambda number : number * (PI/180),
	'fc' : lambda number : (number - 32) * FIVE_OVER_NINE,
	'fk' : lambda number : (number + 459.67) * FIVE_OVER_NINE,
	'ck' : lambda number : number + 273.15,
	'cf' : lambda number : number * NINE_OVER_FIVE + 32,
	'kc' : lambda number : number - 273.15,
	'kf' : lambda number : number * NINE_OVER_FIVE - 459.67
}

def convertion(user_input):
	number_to_covert = float(user_input[:-2])
	function_to_use = list_of_converstions[user_input[-2:]]
	return function_to_use(number_to_covert)

def main():
	while True:
		user_input = input('What to Convert: ')

		try:
			print(convertion(user_input),user_input[-1])
		except KeyError:
			print("Invalid Option of convertion.")
		except: 
			print("invalid Input.")

if __name__=='__main__':
	main()