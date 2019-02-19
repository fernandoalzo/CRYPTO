##############################################################FUNCTIONS####################################################################
def read_file(fichero):
	fichero = "{}".format(fichero)
	try:
		fichero_open = open(fichero, 'r')
		return fichero_open.read()	
	except FileNotFoundError:
		print("the specified file does not exists!!!")
	
def write_file(output_file_name, text_to_write):
	with open(output_file_name,"w") as f:
    	 f.write(text_to_write)    	 

def cypher_fernet(text):
	from cryptography.fernet import Fernet as frnt
	text = str.encode(text)
	#generate key
	random_key = frnt.generate_key()
	#convert to Fernet format key
	key_format_fernet = frnt(random_key)
	cypher = key_format_fernet.encrypt(text)
	#format the ouput
	key = str(random_key).lstrip(" b ").lstrip(" ' ").rstrip(" ' ")	
	cypher_text = str(cypher).lstrip(" b ").lstrip(" ' ").rstrip(" ' ")
	
	data = [key, cypher_text]
	return data
	
def decrypt_fernet(encrypted_text, key):
	from cryptography.fernet import InvalidToken as error
	from cryptography.fernet import Fernet as frnt
	try:
		encrypted_text = str.encode(encrypted_text)
		clave = frnt(key)
		message_decrypted = clave.decrypt(encrypted_text)
		plain_text = str(message_decrypted).lstrip(" b ").lstrip(" ' ").rstrip(" ' ")
		return plain_text
	except ValueError:
		print("Something went wrong with key!!!")
	except error:
		print("Something went wrong!!!")	
