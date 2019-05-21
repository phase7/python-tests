import sys
from math import ceil
m, n, a = map(int, sys.stdin.readline().split(' '))
ans = ceil(m/a) * ceil(n/a)
print (ans)