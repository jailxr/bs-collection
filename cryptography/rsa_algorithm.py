import math
'''
p = 10009, 401, 1019
q = 10039, 409, 1021

'''
p = int(input("Nilai P: "))
q = int(input("Nilai Q: "))
plantext = input("Plan Text: ")
# n = p * q
N = p * q

# m = (p - 1) * (q - 1)
M = (p - 1) * (q - 1)

num_ascc = [ord(i) for i in plantext]
txt_encr, txt_decr = [], []

publicKey  = 0
privateKey = 0
k = 0

def proceed(va, pan, mod):
	foo = va % mod
	for i in range(2,pan+1):
		va = (va*foo) % mod
	return va

# d / public key
i = max([p, q])
while(True):
	if math.gcd(M,i) == 1: 
		publicKey = i
		break
	i+=1

# e / private key
x = 0
while(True):
	x += 1
	if (1 + (x * M)) % publicKey == 0:
		k = x
		privateKey = int((1 + (k * M)) / publicKey)
		break	

print("========================")
print("Nilai N     >> ", N)
print("Nilai M     >> ", M)
print("Public Key  >> ", publicKey)
print("Private Key >> ", privateKey)
print("========================")

# encryption proccess
for x in num_ascc:
	txt_encr.append((x ** int(publicKey)) % N)
num_fixs = "".join([str(x) for x in txt_encr])
print("Plan Text   >> ", plantext)
print("ChipperTeks >> ", num_fixs)

# descryption process
for x in txt_encr:
	txt_decr.append(chr(proceed(x, privateKey, N)))	
num_desc = "".join([i for i in txt_decr])
print("Desk Text   >> ", num_desc)