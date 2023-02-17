from cryptography.fernet import Fernet
import os
import sys
import time

def d():
	title = input('Path/And/Name/Of/Key:\n> ')
	name = title + '.key'
	with open(name, 'rb') as filekey:
		key = filekey.read()

# using the key
	fernet = Fernet(key)

# opening the encrypted file
	print('\n \n		FILE YOU ARE TRYING TO DECRYPT NEEDS TO BE IN SAME DIRECTORY AS THIS, SAME WITH THE KEY \n \n')
	time.sleep(3)
	secFile2 = input('Name Of File You Are Attempting To Decrypt, (including extention .txt, .md, .py, .exe, etc):\n> ')
	with open(secFile2, 'rb') as enc_file:
		encrypted = enc_file.read()

#decrypting the encrypted file
	decrypted = fernet.decrypt(encrypted)

#opening file in write mode
#writing the decrypted data
	with open(secFile2, 'wb') as dec_file:
		dec_file.write(decrypted)



d()
