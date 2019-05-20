# python 3
from pwn import*
from base64 import b64encode, b64decode

from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Cipher import AES

BLOCK_SIZE = 16
KEY_SIZE = 32
NONCE_SIZE = 32

def getRandom(n):
	val = os.urandom(n)
	return val

def encrypt(msg, iv, key):
	msg = pad(msg, BLOCK_SIZE)
	aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
	ciphertext = aes.encrypt(msg)
	return b64encode(ciphertext)

def decrypt(msg, iv, key):
	aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
	msg = b64decode(msg)
	plaintext = aes.decrypt(msg)
	plaintext = unpad(plaintext, BLOCK_SIZE)
	return bytes(plaintext)

r = remote("140.112.31.97", 10158)
n = remote("140.112.31.97", 10158)

txt = r.recvuntil("IV_AB: ")
IV_AB = r.recvline().strip()
IV_AB = b64decode(IV_AB)

### Part 1: Initial ###
Nx = getRandom(KEY_SIZE)
txt = r.recvuntil("> "); r.sendline("1")
txt = r.recvuntil("> "); r.sendline("A||" + str(b64encode(Nx), 'utf-8'))

txt = r.recvuntil("B -> S: ")
lst = str(r.recvline().strip())[2:-1]
lst = lst.split("||")[2]

txt = r.recvuntil("Nr: ")
Nr = str(r.recvline().strip())[2:-1]

txt = r.recvuntil("msg1: ")
msg1 = str(r.recvline().strip())[2:-1]

txt = r.recvuntil("msg2: ")
msg2 = str(r.recvline().strip())[2:-1]

r.sendline(str(encrypt(b64decode(Nr), IV_AB, Nx))[2:-1] + "||" + lst)
txt = r.recvuntil("flag: ")
flg = str(r.recvline().strip())[4:-2]
flg = decrypt(flg, IV_AB, Nx)
print (flg)

### BALSN{M1dT3rM_i5_S0_h4rD_QAQ}

### Part 2: Subsequent ###
Nx = getRandom(KEY_SIZE)
txt = r.recvuntil("> "); r.sendline("2")
txt = r.recvuntil("> "); r.sendline(str(b64encode(Nx), 'utf-8') + "||" + msg1)

txt = r.recvuntil("Nb: ")
Nb = str(r.recvline().strip())[2:-1]

txt = r.recvuntil("msg2: ")
msg2 = str(r.recvline().strip())[2:-1]

txt = n.recvuntil("> "); n.sendline("2")
txt = n.recvuntil("> "); n.sendline(Nb + "||" + msg1)

txt = n.recvuntil("Nb: ")
Nb = str(n.recvline().strip())[2:-1]

txt = n.recvuntil("msg2: ")
msg2 = str(n.recvline().strip())[2:-1]

r.sendline(msg2)
r.interactive()

### BALSN{R3fl3Ct1oN_4774cK_S0_p0w3RfuL}