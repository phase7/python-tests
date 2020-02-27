import hashlib

string1 = "Practical Cryptography"

md5_str = hashlib.md5(string1.encode('utf-8')).hexdigest()

print("MD5 for "+ string1 +" is " + md5_str)

string2 = "Ratul Roy" #Full name

md5_str = hashlib.md5(string2.encode('utf-8')).hexdigest()

print("MD5 for "+ string2 +" is " + md5_str)

sha1_str = hashlib.sha1(string1.encode('utf-8')).hexdigest()

print("SHA1 for "+ string1 +" is " + sha1_str)

sha1_str = hashlib.sha1(string2.encode('utf-8')).hexdigest()

print("SHA1 for "+ string2 +" is " + sha1_str)