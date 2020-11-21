def delare_minus_specallfall(num):
	retlist=[]
	for a in range(1,num+1):
		if ((num % a) == 0):
			if a % 2 == 0 and a % 50 != 0: #kontroll att delaren stämmer överäns med special fall
				retlist += [a]
	return retlist

print(len(delare_minus_specallfall(32200)))
