from pwn import*

r = remote("140.112.31.97", 10162)

txt = r.recvuntil("UUID:\n")
buf = b'2b59e59e-0c25-421c-96d1-4670f6baee01ffffffffffffffffffffffff'.decode("utf-8")
r.sendline(buf)

txt = r.recvline()
res = r.recvline().strip("\n")
print res

# flag: BALSN{P4tH_3xpl0s!oN_b0oo0oO0o0oOO0ooOM}