def get_prob(num_of_sides,  hp):
	probability = pow(1/num_of_sides,int(hp/num_of_sides))
	if not hp % num_of_sides == 0:
		probability *= (1 + num_of_sides - hp % num_of_sides) / num_of_sides
	return probability

print(get_prob(400,200))