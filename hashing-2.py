import hashlib
import secrets

# Generate a random salt using the secrets module
salt = secrets.token_hex(16)
print("Salt:", salt)

# Get the user's password from input
password = input("Enter your password: ")
print("Password:", password)

# Hash the password using the salt and the SHA-256 algorithm
hash_object = hashlib.sha256((password + salt).encode())
print("Hash:", hash_object)

# Get the hexadecimal representation of the hash
hash_hex = hash_object.hexdigest()
print("Hash (hex):", hash_hex)

# Get the user's password from input
new_password = input("Enter your password again: ")

# Hash the password using the salt and the SHA-256 algorithm
new_hash_object = hashlib.sha256((new_password + salt).encode())

# Get the hexadecimal representation of the new hash
new_hash_hex = new_hash_object.hexdigest()

if new_hash_hex == hash_hex:
	print("The passwords match.")
else:
	print("The passwords do not match.")