import sys

array_of_input = [line_to_split.rstrip('\n') for line_to_split in sys.stdin]

biggest_line_count = len(max(array_of_input, key=len))

for each_array_slot in range(biggest_line_count):
	for each_array in array_of_input:
		if each_array_slot < len(each_array):
			print(each_array[each_array_slot], end='')
		else:
			print(' ', end='')
	print(' ')