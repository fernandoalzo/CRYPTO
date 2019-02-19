import sys
#sys.path.append("..")
from stl import style as stl 
from opt import options as opt
from func import functions as func
#arguments
args = sys.argv
#num arguments
num_args = len(args)

if(num_args == 1):
	opt.help()
	
elif(num_args == 2):
	if(args[1] == '-c' or args[1] == '--cypher'):
		text_to_encrypt = input(stl.FONDO_VERDE(stl.NEGRITA("Write the text that you want to encrypt: \n\n")))
		encryptor = func.cypher_fernet(text_to_encrypt)
		key = encryptor[0]
		cipher_text = encryptor[1]
		
		print(stl.FONDO_ROJO(stl.NEGRITA("key: ")) + key)
		print(stl.FONDO_ROJO(stl.NEGRITA("cipher text: ")) + cipher_text)		
					
	elif(args[1] == '-d' or args[1] == '--decrypt'):
		encrypted_text = input(stl.FONDO_VERDE(stl.NEGRITA("Write the encrypted tex: \n")))
		key = input(stl.FONDO_VERDE(stl.NEGRITA("Write the key: \n")))
		plain_text = func.decrypt_fernet(encrypted_text, key)		
		print(stl.FONDO_VERDE(stl.NEGRITA("===============PLAIN TEXT===============\n\n")))
	
		print(plain_text)		
		
	elif(args[1] == '-i'):
		print(""" 
		.
		interactive mode here
		.
		""")
		
	elif(args[1] == '-a' or args[1] == '--algorithm'):
		print("""		.
		algorithm selectio here		.
		""")
	else:
		print("invalid option")
		
elif(num_args == 4 ):
	if(args[1] == "-c" or args[1] == "--cypher" and args[2] == '-f'):
	
		print("cifrando...")
		file_to_cipher = func.read_file(args[3])
		cipher_text = func.cypher_fernet(file_to_cipher)		
		print(stl.FONDO_VERDE("KEY: ") + cipher_text[0])
		print(stl.FONDO_ROJO("CIPHER TEXT: ") + cipher_text[1])	
		#key:
		
		
	elif(args[1] == "-c" or args[1] == "--cypher" and args[2] == "-o"):
		print("ha selecionado la opcion de cifrar con la salida hacia un archivo")
		
		
	elif(args[1] == '-d' or args[1] == '--decrypt' and args[2] == '-f'):
		print("""		
		decrypt the text specified		
		""")
		
elif(num_args == 3):
	print("Missing arguments!!!")



elif(num_args == 4):
	if(args[1] == "-c" or args[1] == "--cypher" and args[4] == "-o" or args[4] == "--output"):
		print("cifrado con salida en un archivo llamando {}".format(args[5]))
