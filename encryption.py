from math import floor, ceil, sqrt

inp = input()
txt = ''.join(inp.split())
#print(txt)
l = len(txt)
tmp = sqrt(l)
row = floor(tmp)
col = ceil(tmp)
fill = col - (l % col)
print(l,tmp,row,col, fill)

lst = []
lst.append(list(txt[0:col]))
for i in range(row-1):
	lst.append(list(txt[((i+1)*col):((i+2)*col)]))
# for _ in range(fill):
# 	lst[-1].append('')
print(lst)
