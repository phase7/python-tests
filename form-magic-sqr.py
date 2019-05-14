pre = [     
		[8, 1, 6, 3, 5, 7 ,4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
      ]

s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))
mat = [elem for row in s for elem in row] #flatten the matrix into one single list
s.clear()

for i in range(8):
	matc = pre[i]
	total_dif = 0
	for j in range (len(matc)):
		total_dif += abs(matc[j] - mat[j])
	s.append(total_dif)
	#print(s)
print(min(s))
