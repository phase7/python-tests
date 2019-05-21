
loop = input()
o_disk = input()
c_disk = input()

moves = 0
list = [0, 0]

for i in range(int(loop)):
	list[0] = abs(int(o_disk[i]) - int(c_disk[i]))
	list[1] = 10 - list[0]
	moves += min(list)

print (moves)