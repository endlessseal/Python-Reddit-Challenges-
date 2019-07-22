import itertools
def find_max_digit(num):
	return max(str(num))

def arrange_largest_num(num, mode=True, number_of_digits=4):
	return int(''.join(sorted(str(num).zfill(number_of_digits), reverse=mode)))

def counting_iteration_for_Kaprekar(num):
	answer = num
	for iteration in itertools.count(1):
		if arrange_largest_num(answer) == 7641:
			return iteration
		else:
			answer = arrange_largest_num(answer) - arrange_largest_num(answer,False)

print(counting_iteration_for_Kaprekar(5455))