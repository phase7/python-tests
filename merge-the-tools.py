string, k = input(), int(input())

from collections import Counter
len  = len(string)
sublen = len // k

str_list = list(string)
substring = [str_list[s:s+sublen] for s in range(0, len, sublen) ]
#print(substring)

for item in substring:
	c = Counter(item)
	rev_it = item.reverse()
	for 