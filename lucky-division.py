ln = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

tst = int(input())

for x in ln:
	if tst == x:
		print("YES")
		break
	if tst > x:
		if 0 == tst % x:
			print("YES")
			break
		elif 777 == x:
			print("NO")
			break
		else:
			continue
	print("NO")
	break
