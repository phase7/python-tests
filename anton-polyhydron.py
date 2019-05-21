import sys

ans = 0
val_of = dict(Tetrahedron = 4, Cube = 6, Octahedron = 8, Dodecahedron = 12, Icosahedron = 20)
idx = int(input())

for i in range(idx):
	poly = input()
	ans += val_of[poly]

print(ans)
