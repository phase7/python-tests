from bisect import insort

lst = [6,8,9,44,55,66,52,100]
print(lst)

insort(lst, 23)

print("\ninserting 23 in middle", lst, sep='\n')