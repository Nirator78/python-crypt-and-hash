import hashlib

message = "Hello, World!"
print(message)

hash_value = hashlib.md5(message.encode()).hexdigest()

print(hash_value)
# Impossible to reverse the hash value to get the original message