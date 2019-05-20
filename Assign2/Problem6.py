# python 2
from pwn import*
import os
import time
import random
import hashlib
import pickle

PERTURB_SHIFT = 5

def sha256(content):
	Hash = hashlib.sha256()
	Hash.update(content)
	return Hash.digest()

def sha256Try(lst, ind):
	for item in range(33, 93):
		lst[ind] = chr(item)

		if ind == 0:
			value = sha256(''.join(lst)).encode("hex")[-6:]
			sha256Dic[value] = ''.join(lst)
		else:
			sha256Try(lst, ind - 1)
	return

def sha256BuildDic():
	global sha256Dic
	if os.path.exists('sha256Dic.pickle'):
		with open('sha256Dic.pickle', 'rb') as f:
			sha256Dic = pickle.load(f)

	else:
		lst = []
		sha256Dic = {}
		for k in range(4):
			lst.append("")
			sha256Try(lst, k)
		
		with open('sha256Dic.pickle', 'wb') as f:
			pickle.dump(sha256Dic, f)
		return sha256Dic

### Part 1: Challenge ###
r = None
sha256BuildDic()
while True:
	r = remote("140.112.31.97", 10159)

	txt = r.recvuntil("ends with ")
	key = r.recvuntil(": ")[:-2]
	
	try:
		ans = sha256Dic[key]
		r.sendline(ans.encode("hex"))
		r.recvuntil("attempt.")
		break
	
	except KeyError:
		r.close()

### Part 2: Denial ###
itr = 1
perturb = 1
r.sendline("50000")
f = open('input6.txt', 'w')
for k in range(2**15):
	itr = 5 * itr + 1 + perturb
	itr = itr & 131071
	perturb >>= PERTURB_SHIFT

	r.sendline(str(itr))
	f.write(str(itr) + "\n")

for k in range(50000 - 2 **15):
	r.sendline('1073732922')
	f.write('1073732922\n')
f.close()

txt = r.recvuntil("flag:\n")
ans = r.recvline().strip()
print ans

# BALSN{Py7h0n_4lg@r!thmic_Comp13Xity_Att4ck}