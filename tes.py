def nmaxnumber(lis,n):
	final = []
	for i in range(0,n):	
		max1 = 0
		for j in range(len(lis)):
			if lis[j] > max1:
				max1 =  lis[j]
		lis.remove(max1)
		final.append(max1)
	print final
lis = [81,52,45,10,3,2,96]
n = 2
nmaxnumber(lis,n)
