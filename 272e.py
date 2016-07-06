from collections import OrderedDict

quit = ''
bag_of_letters =  {'A':[9,1], 'B':[2,3], 'C':[2,3], 'D':[4,2], 'E':[12,1], 'F':[2,4], 'G':[3,2], 
				'H':[2,4], 'I':[9,1], 'J':[1,8], 'K':[1,5], 'L':[4,1], 'M':[2,3], 'N':[6,1],
				'O':[8,1], 'P':[2,3], 'Q':[1,10], 'R':[6,1], 'S':[4,1], 'T':[6,1], 'U':[4,1],
				'V':[2,4], 'W':[2,4], 'X':[1,8], 'Y':[2,4], 'Z':[1,10], '_':[2,0]}

def remove_from_bag(word):
	global bag_of_letters 
	for each_character in word:
		if bag_of_letters[each_character][0]-1 < 0:
			print('There is not enough letters for you to build that word.') 
			return
		else:
			bag_of_letters[each_character][0] -= 1
	for every_letter in reversed(OrderedDict(sorted(bag_of_letters.items(), key = lambda x: (x[1], x[0]))).items()):
		print(every_letter[0] + ' has %d left in the bag.' % every_letter[1][0])

while not quit == 'T':
	s = input('Enter word to remove from bag: ')
	remove_from_bag(s.upper())
	quit = input('Type T to quit else enter anything to continue: ')
