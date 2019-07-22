from itertools import permutations

def solve(m):
	num_of_set = len([i for i in m if i.isdigit() or i == 'x'])
	if num_of_set % 9 == 0:
		l = list(range(1,10))*num_of_set
		for i in list(m): 
			if i.isdigit():
				l.remove(int(i))
		for p in permutations(l,m.count('x')): 
			x = m.replace('x','{}').format(*p).split('=')
			s1 = sum([int(s) for s in x[0].split('+')])
			s2 = sum([int(s) for s in x[1].split('+')]) 
			if s1 == s2:
				return "=".join(x).strip()
		else:
			return "no combo"
	else:
		return "not possible to use of all 9 digits"
		
print(solve("xxx + xxx = 468"))