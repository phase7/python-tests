import sys

a, b = map(int, sys.stdin.readline().split(' '))
inc = 0

while a <= b:
	a = a * 3
	b = b * 2
	inc = inc + 1

print(inc)