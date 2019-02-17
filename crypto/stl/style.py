"""
formato = [A;Bm
formato = [A;B;Cm

A es un dígito que indica formato:
0 - normal
1 - negrita
2 - diluir
3 - cursiva
4 - subrayado
5 - parpadeo lento
6 - parpadeo rápido
7 - negativo (invertir)

B es un número que indica el color de letra:

INTENSIDAD NORMAL: 30, 31, 32, 33, 34, 35, 36, 37
INTENSIDAD FUERTE: 90, 91, 92 ,93, 94, 95, 96 ,97 


C es un numero que indica el color de fondo:

INTENSIDAD NORMAL: 41, 42, 43, 44, 45, 46, 47
INTENSIDAD FUERTE: 100, 101, 102, 103, 104, 105, 106, 107
"""

#FUNCIONES

#personalizado

def PERSONALIZADO(TEXTO, FORMATO, COLOR_TEXTO, FONDO):
	EDITADO = chr(27) + "[%i;%i;%im"%(FORMATO, COLOR_TEXTO, FONDO) + TEXTO + chr(27) + "[0m" 
	
	return EDITADO


def NEGRITA(TEXTO):
	EDITADO = chr(27) + "[1m" + TEXTO + chr(27) + "[0m"

	return EDITADO


def NEGRITA_COLOR(TEXTO, COLOR_TEXTO):
	EDITADO = chr(27) + "[1;%im"%(COLOR_TEXTO) + TEXTO + chr(27) + "[0m" 

	return EDITADO


def SUBRAYADO(TEXTO):
	EDITADO = chr(27) + "[4m" + TEXTO + chr(27) + "[0m"
	
	return EDITADO


def CENTRAR_TEXTO(TEXTO):
	EDITADO = chr(27) + "[1m" + TEXTO.center(100, "=") + chr(27) + "[0m"
	return EDITADO
	


#color de textos

def TEXTO_ROJO(TEXTO):
	EDITADO = chr(27) + "[0;31m" + TEXTO + chr(27) + "[0m"
	
	return EDITADO

def TEXTO_VERDE(TEXTO):
	EDITADO = chr(27) + "[0;32m" + TEXTO + chr(27) + "[0m" 

	return EDITADO
	
def TEXTO_AMARILLO(TEXTO):
	EDITADO = chr(27) + "[0;33m" + TEXTO + chr(27) + "[0m" 

	return EDITADO


def TEXTO_AZUL(TEXTO):
	EDITADO = chr(27) + "[0;34m" + TEXTO + chr(27) + "[0m"
		
	return EDITADO

def TEXTO_MORADO(TEXTO):
	EDITADO = chr(27) + "[0;35m" + TEXTO + chr(27) + "[0m"

	return EDITADO


def TEXTO_CIAN(TEXTO):
	EDITADO = chr(27) + "[0;36m" + TEXTO + chr(27) + "[0m"

	return EDITADO

#color de fondos

def FONDO_ROJO(TEXTO):
	EDITADO = chr(27) + "[1;41m" + TEXTO + chr(27) + "[0m"

	return EDITADO


def FONDO_VERDE(TEXTO):
	EDITADO =  chr(27) + "[1;42m" + TEXTO + chr(27) + "[0m"

	return EDITADO

def FONDO_AMARILLO(TEXTO):
	EDITADO = chr(27) + "[1;43m" + TEXTO + chr(27) + "[0m"

	return EDITADO

def FONDO_AZUL(TEXTO):
	EDITADO = chr(27) + "[1;44m" + TEXTO + chr(27) + "[0m"

	return EDITADO

def FONDO_MORADO(TEXTO):
	EDITADO = chr(27) + "[1;45m" + TEXTO + chr(27) + "[0m"

	return EDITADO

def FONDO_CIAN(TEXTO):
	EDITADO = chr(27) + "[1;46m" + TEXTO + chr(27) + "[0m"

	return EDITADO
