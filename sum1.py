def sum_range_multiples_3_5(min, max):
	total = 0
	for i in range(min,max):
		if (i % 3 == 0) or (i % 5 == 0):
			total += i
	return total