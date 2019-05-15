from collections import Counter

item = list('aaba')
c = Counter(item)
item.reverse()
# len2 = len(item)
for k in c.keys():
	for i in range(c[k] - 1):
		item.remove(k)
item.reverse()
