
p = 47
q = 71
k = 25
# n = p * q
N = p * q

# m = (p - 1) * (q - 1)
M = (p - 1) * (q - 1)
publicKey  = 79
privateKey = 1 + (k * M) / publicKey
text = 'HI DEAR, IT\'S ME JAILANI WHO LOVE U SO MUCH'

num_ascc = [ ord(i) for i in text]
txt_encr, txt_decr = [], []

for x in num_ascc:
	txt_encr.append((x ** int(publicKey)) % N)
num_fixs = "".join([str(x) for x in txt_encr])

print("Text >>", text)
print("ChipperTeks >>", num_fixs)

for x in txt_encr:
	txt_decr.append(chr(((x ** int(privateKey)) % N)))	
num_desc = "".join([i for i in txt_decr])

print("Deskripsi", num_desc)