string, k = input(), int(input())

from collections import Counter
l  = len(string)
sublen = l // k

str_list = list(string)
substring = [str_list[s:s+sublen] for s in range(0, l, sublen) ]
#print(substring)

for item in substring:
	c = Counter(item)
	item.reverse()
	for k in c.keys():
		for i in range(c[k] - 1):
			item.remove(k)
	item.reverse()
	print(''.join(item))
