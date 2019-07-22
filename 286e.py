import itertools
def solve(num):
	for iteration in itertools.count(1):
		num = num / iteration
		if num == 1:
			return iteration
		elif 0<=num<1:
			return None

print(solve(720))