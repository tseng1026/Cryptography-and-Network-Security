# python 2
import os
import sys
import base64
import random
import hashlib
import hashpumpy
from pwn import*

r = remote("140.112.31.96", 10154)

# get the token
txt = r.recvuntil("> "); r.sendline("2")
txt = r.recvuntil("> "); r.sendline("2")
txt = r.recvuntil("Token: ")
tok = r.recvline().strip("\n")

# pump with the padding string
for k in range(44, 55):
	txt = r.recvuntil("> "); r.sendline("3")
	cph, msg = hashpumpy.hashpump(tok, "2", "hidden_flag=!;P%*&BALSN_Coin=2147483548", 4 + k + 12)
	print msg

	msg = base64.b64encode(msg)
	txt = r.recvuntil("\n> "); r.sendline(msg)
	txt = r.recvuntil("\n> "); r.sendline(cph)

	txt = r.recvline()
	if txt != "Invalid Token\n": break
	# flag: BALSN{L3ngTh_3xeT3n5i0N_4tTacK_i5_34sY_w1tH_H4shPump}

r.interactive()
r.close()