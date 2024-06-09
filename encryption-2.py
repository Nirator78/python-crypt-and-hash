import rsa
 
publicKey, privateKey = rsa.newkeys(512)
print("Public key: ", publicKey)
print("Private key: ", privateKey)
 
message = "Hello, World !"
 
encMessage = rsa.encrypt(message.encode(), publicKey)
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
decMessage = rsa.decrypt(encMessage, privateKey)
 
print("decrypted string: ", decMessage.decode())
