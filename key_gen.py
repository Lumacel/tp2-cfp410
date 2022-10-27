import random

def gen_password(longitud):	
	
	password=""
	for l in range(longitud):
		password += chr(random.randint(33,125)) #agrega caracter random ASCII (entre 33 y 125)

	return password

if __name__ == "__main__":
	print(gen_password(5))