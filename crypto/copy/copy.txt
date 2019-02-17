from cryptography.fernet import Fernet

print("CIFRADO:")
text = str.encode(input("digite el texto que desa cifrar: "))
key = Fernet.generate_key()
print(type(key))
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(text)

print(str(key).rstrip(" ' ").lstrip(" b ").lstrip(" ' "))
#print("clave" + str(key))
print(str(cipher_text).rstrip(" ' ").lstrip(" b ").lstrip(" ' "))
#print(cipher_text)

print("DESCIFRADO:")
texto_cifrado =str.encode(input("digite su texto cifrado: "))
clave = Fernet(input("digite su clave de cifrado: "))
mensaje = clave.decrypt(texto_cifrado)
print(str(mensaje).rstrip(" ' ").lstrip(" b ").lstrip(" ' "))
