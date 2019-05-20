# python 3
from pwn import*
import numpy as np
import random
import time
import base64
np.set_printoptions(threshold=sys.maxsize)
# def gen_keys():
# 	random.seed(1234)
# 	keys = []
# 	for i in range(64):
# 		keys += [[1 for i in range(48)]]
# 	return keys

# def encrypt(text, key):
# 	return [text[i] ^ key[i] for i in range(48)]

mat = np.zeros((256, 65))
flg = []

# keys = gen_keys()
i = 0
while i < 256:
	r = remote("140.112.31.96", 10153)

	## generate
	t = time.time()
	random.seed(int(t))
	key = random.randint(0,(2**64)-1)
	# flag = "FLAGXXXXXXFLAGXXXXXXFLAGXXXXXXFLAGXXXXXXFLAGXXXX"
	# secret = [ord(c) for c in flag]
	# for j in range(64):
	# 	if key & (2**j) != 0:
	# 		secret = encrypt(secret, keys[j])

	for j in range(64):
		if key & (2**j) != 0: mat[i][j] = 1
	mat[i][64] = 1

	txt = r.recvline().strip()
	# txt = str(base64.b64encode(bytes(secret)))[2:-1]
	txt = str(base64.b64decode(txt))[2:-1]
	txt = [ord(c) for c in txt]
	
	if t - int(t) > 0.2 or t - int(t) < 0.8: 
		flg.append(txt)
		i = i + 1

	r.close()
	sleep(1)

print (mat)
print (flg)

print ("===============================")
for j in range(65):
	# swap the row
	if mat[j][j] == 0: 
		for i in range(j + 1, 256):
			if mat[i][j] != 0: 
				mat[i] = np.logical_xor(mat[i], mat[j])
				mat[j] = np.logical_xor(mat[i], mat[j])
				mat[i] = np.logical_xor(mat[i], mat[j])

				tmp = flg[i]
				flg[i] = flg[j]
				flg[j] = tmp
				break

	# xor the ciphertext
	if mat[j][j] != 0:
		for i in range(j + 1, 256):
			if mat[i][j] != 0:
				mat[i] = np.logical_xor(mat[i], mat[j])
				flg[i] = [flg[i][k] ^ flg[j][k] for k in range(48)]

	print (mat)
	print (flg)
for i in range(256):
	res = flg[i]
	res = [chr(c) for c in res]
	res = "".join(res)
	print(res)