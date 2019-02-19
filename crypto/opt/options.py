from stl import style as stl 

def help():
	print(stl.NEGRITA("""  
	
 ██░ ██ ▓█████  ██▓     ██▓███                 
▓██░ ██▒▓█   ▀ ▓██▒    ▓██░  ██▒               
▒██▀▀██░▒███   ▒██░    ▓██░ ██▓▒               
░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██▄█▓▒ ▒               
░▓█▒░██▓░▒████▒░██████▒▒██▒ ░  ░ ██▓  ██▓  ██▓ 
 ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░▒▓▒░ ░  ░ ▒▓▒  ▒▓▒  ▒▓▒ 
 ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░▒ ░      ░▒   ░▒   ░▒  
 ░  ░░ ░   ░     ░ ░   ░░        ░    ░    ░   
 ░  ░  ░   ░  ░    ░  ░           ░    ░    ░  
                                  ░    ░    ░  

	python3 tools.py -cd
	python3 tools.py -cd -f [file_name] -o [output_file]
	 
	[1]. -c --cypher
 	  	encrypt message.
 
 	[1.1]. -f --file 
 		Reads the contents of the file and encrypts it.
  
	[2]. -d --decrypt.
  		decrypt message.
 
  	[2.1]. -f --file
 		Reads the encrypted content of the file and decrypts it. 		
	
	[3]. -i.
  	 	interactive mode.
	
	[4]. -a --algorithm
	   	choose encryption algorithm.

		   	
	"""))
