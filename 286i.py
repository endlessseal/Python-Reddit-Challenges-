def fib_list(max_num, x=3):
	list_of_fib = [1,1]
	while x < max_num:
		x = list_of_fib[-1] + list_of_fib[-2]
		list_of_fib.append(x)
	return list_of_fib
	
def find_num_smaller(num, my_list):
	for value in reversed(my_list):
		if value <= num:
			return value 
	
def solve(num):
	combo_list = []
	list_to_pick_from = fib_list(num)
	while num > 0:
		temp_value = find_num_smaller(num,list_to_pick_from)
		num -= temp_value
		combo_list.append(temp_value)
	print(combo_list)

solve(1337)