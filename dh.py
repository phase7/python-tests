import sys;

noofarg = len(sys.argv);
g = 6;
p = 13;

def help_string():
	print(" DH.py has two functions -\n\
	DH.py private_key > outputs the public key\n\
	DH.py private_key public_key > outputs the session key\
	 ")


if ( noofarg < 2 or noofarg > 3 ):
	print ("Invalid no. of argument")
	help_string();

elif (noofarg is 2):
	prk = int(sys.argv[1]);
	print((g**prk)%p);


elif (noofarg is 3):
	prk = int(sys.argv[1]);
	puk = int(sys.argv[2]);
	print((puk**prk)%p);

