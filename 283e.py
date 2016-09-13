def build_dictionary(word):
	temp_dict = {}
	for each in word:
		try:
			temp_dict[each] += 1
		except KeyError:
			temp_dict[each] = 1
			continue
	return temp_dict

def compare_words(word):
	i = iter(word.replace('"','').replace(" ",'').split('?'))
	first_sent = next(i)
	d0 = {}
	for second_sent in i:
		
		if ''.join(sorted(first_sent)) == ''.join(sorted(second_sent)):
			print("Doesnt match cause words just scramble")
			return 1
		
		if not d0:
			d0 = build_dictionary(first_sent)	
			d1 = build_dictionary(second_sent)
		else:
			d0 = d1
			d1 = build_dictionary(second_sent)
		
		d0k = sorted(list(d0.keys()))
		d1k = sorted(list(d1.keys()))

		if d0k <= d1k:
			for each_key in d1k:
				if d1[each_key] > d0[each_key]:
					print("Sentence two has more of one letters")
					return 1
		else:
			print("Sentence two contain different letters")
			return 1
	print("It works")

compare_words('"client eastwood" ? "old west action" ? "old west act"')
compare_words('"pass this" ? "this pass"') 
