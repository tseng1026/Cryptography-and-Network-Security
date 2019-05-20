# python 2
from pwn import*

r = remote("140.112.31.96", 10151)

### Warmup1 ###
txt = r.recvuntil("[>]: ")
r.sendline("2")

### Warmup2 ###
txt = r.recvuntil("text = ")
tmp = r.recvline().strip("\n")
r.sendline(tmp)

### Round1 ###
txt = r.recvuntil("c1 = ")
tmp = r.recvline().strip("\n")

for i in range(26):
	res = ""
	for k in range(len(tmp)):
		char = tmp[k]

		if (char.isupper()): res += chr((ord(char) + i - 65) % 26 + 65)
		elif (char.islower()): res += chr((ord(char) + i - 97) % 26 + 97)
		else: res += tmp[k]
	
	print res

tmp = raw_input("Solutions: ").strip("\n")
r.sendline(tmp)

### Round2 ###
txt = r.recvuntil("c1 = ")
cph = r.recvline().strip("\n")
txt = r.recvuntil("m1 = ")
msg = r.recvline().strip("\n")

lst = [0, 0, 0, 0, 0, 0, 0]
for k in range(len(msg)):
	if (lst[k % 7] == 0): lst[k % 7] = (ord(cph[k]) - ord(msg[k]) + 26) % 26

txt = r.recvuntil("c2 = ")
tmp = r.recvline().strip("\n")
res = ""
for k in range(len(tmp)):
	char = tmp[k]
	if (char.isupper()): res += chr((ord(char) - lst[k % 7] + 26 - 65) % 26 + 65)
	elif (char.islower()): res += chr((ord(char) - lst[k % 7] + 26 - 97) % 26 + 97)
	else: res += tmp[k]
r.sendline(res)

### Round3 ###
txt = r.recvuntil("c1 = ")
cph = r.recvline().strip("\n")
txt = r.recvuntil("m1 = ")
msg = r.recvline().strip("\n")

key = 0
for k in range(len(msg)):
	if (msg[k] == cph[1] and msg[2 * k] == cph[2]): key = k; break

txt = r.recvuntil("c2 = ")
tmp = r.recvline().strip("\n")

tot = []
for i in range(key / 2):
	tot.append(len(tmp) / key * 2)
	if (i % (key / 2) == 0): tot[i] -= len(tmp) / key
	if (len(tmp) % key > i): tot[i] += 1
	if (i != 0): tot[i] += tot[i - 1]
tot.insert(0, 0)

rnd = -1
res = ""
for k in range(len(tmp)):
	if (k % key == 0): 
		rnd += 1
		res += tmp[tot[k % key] + rnd]

	elif (k % key == key / 2):
		res += tmp[tot[k % key] + rnd]

	elif (k % key < key / 2):
		res += tmp[tot[k % key] + rnd * 2]

	elif (k % key > key / 2): 
		res += tmp[tot[key - k % key] + rnd * 2 + 1]
r.sendline(res)

### Round4 ###
# base64 hash function
r.interactive()

# flag: BALSN{CRYPT0_1S_3ASY_XDD}
r.close()