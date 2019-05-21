n = int(input())
ans = 0

for x in range(n -1 ):
	ans += n + x * (n - x)

print (ans + 1 - n)