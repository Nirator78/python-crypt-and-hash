from cryptography.fernet import Fernet

message = "Hello, World"

key = Fernet.generate_key()

print(message)
print(key)

cipher_suite = Fernet(key)

cipher_text = cipher_suite.encrypt(message.encode())

print(cipher_text)

plain_text = cipher_suite.decrypt(cipher_text)

print(plain_text.decode())