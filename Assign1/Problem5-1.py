# python 3
from pwn import*
import random
import time
import base64

r = remote("140.112.31.96", 10152)
par = int(time.time())

cph = r.recvline().strip()
cph = bytes(base64.b64decode(cph))

while True:
	random.seed(par)
	lst = [chr(i ^ random.randint(0,255)) for i in cph]
	res = ''.join(lst)
	
	if res[0:5] == "BALSN":
		print(res)
		break

		# flag: BALSN{7ime_Se3d_Cr4ck!n9}
		r.close()

	par = par + 1