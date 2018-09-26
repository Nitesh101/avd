str1 = ['nitesh','suresh','sathish','nitesh','nitesh','suresh']#input("Enter a name: ")
str2 = [1,2,3,4,5,6]#input("Enter marks: ")
d = {}
for i in range(len(str1)):
	if (str1[i]) in d.keys():
		d[str1[i]].append(str2[i])
	else:
		d[str1[i]] = []
		d[str1[i]].append(str2[i])
print "the name and marks of studets",d
