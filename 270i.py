import string
#test_string = '\"attack.\" In fact, Yeoman Tamura\'s tricorder shows that Kirk has been killed after beaming down to the bridge, Kirk reminisces about having time to beam down. Kirk wants Spock to grab hold of him in a fist fight with Kirk and Spock try to escape, the collars are activated, subjecting them to an entrance, which then opens. Scotty saves the day by pretending to help Spock, and Mullhall voluntarily agree, and the others transported to the one which is not at all obvious what to make diplomatic advances. Meanwhile Kirk isable to get inside. McCoy and nerve pinches Chief at'
test_string = 'Now is not the time for desert, now is the time for dinner'


def create_lookup_table(str, size_of_prefix):
	try:
		list_of_words = [x.lower() for x in ''.join(ch for ch in str if ch not in set(string.punctuation)).split(' ')]
		print(list_of_words)
	except:
		print("Not a valid String Input, Could not be split")
		raise

	my_dict = dict()

	for counter in range(size_of_prefix, len(list_of_words)):
		first_word, second_word, third_word = list_of_words[counter-2:counter+1]
		if (first_word,second_word) not in my_dict:
			my_dict[first_word,second_word] = {}
		if third_word not in my_dict[first_word,second_word]:
			my_dict[first_word,second_word][third_word] = 0
		my_dict[first_word,second_word][third_word] += 1

	return my_dict
print(create_lookup_table(test_string,2))