def length_count(num):
	d = {}
	for i in num:
		keys=d.keys()
		if i in keys:
			d[i] += 1
		else:
			d[i] = 1
	return d
print(length_count('ggsjshd'))
