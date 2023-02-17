from cryptography.fernet import Fernet
import os
import sys
import time

def e():
#opens key
	title = input('Path/And/Name/Of/Key:\n> ')
	name = title + '.key'
	with open(name, 'rb') as filekey:
		key = filekey.read()

#using the generated key
	fernet = Fernet(key)

#opens file to encrypt
	print('		KEY AND FILE TRYING TO ENCRYPT NEED TO BE IN THE SAME DIRECTORY AS THIS PROGRAM')
	time.sleep(3)
	secFile = input('Name Of File (including extention .txt, .md, .py, etc):> ')
	with open(secFile, 'rb') as file:
		original = file.read()

#encrypting the file
	encrypted = fernet.encrypt(original)

#opening file in write mode
#writing the encrypted data
	with open(secFile, 'wb') as encrypted_file:
		encrypted_file.write(encrypted)



e()
