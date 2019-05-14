inp = 'aAaAaAaAkianvuUieneillsowPacjjdjsuuauuuusiekOOoosoisIIIkiIjjJj'
l = len (inp)
inp = list(inp)

for i in range(l-2):
	if inp[i].lower() == inp[i+1].lower() == inp[i+2].lower() :
		inp[i+2] = ''

for it in inp:
	print (it, end='')