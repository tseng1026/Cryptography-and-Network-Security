# python 2
# reference: https://github.com/thereal1024/python-md5-collision
from pwn import*
import base64
import hashlib

r = remote("140.112.31.96", 10150)

cph1 = "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMgojIC0qLSBjb2Rpbmc6IHV0Zi04IC0qLQojICAgICAKZGlmZiA9ICcnJ98Hz82TPjrt8TjrMQKaUaa6n2Reo+9RdjByeypIoCjyERXt8jrj227nH9nb19M3KXQKgm2Er37UCCCIAShu8Se3OWeh32mR92gyAXmG9rR2xbFt/MvoDO9uG+BLS2DjQbEovaoSCZOeZqFrkcm9gQvw2DYP8XPkxFFpqskFBJi9JycnCnNhbWUgPSAnJyffB8/Nkz467fE46zECmlGmup9k3qPvUXYwcnsqSKAo8hEV7fI649tu5x/Z29dTNyl0CoJthK9+1AggiIEobvEntzlnod9pkfdoMgF5hva0dsWxbXzL6AzvbhvgS0tg40GxKL2qEgmTnmaha5HJPYIL8Ng2D/Fz5MRRaapJBQSYvScnJwoKaWYgKHNhbWUgPT0gZGlmZik6CiAgICBwcmludCAiTUQ1IGlzIHNlY3VyZSEiCgplbHNlOgogICAgcHJpbnQgIkp1c3Qga2lkZGluZyEiCgo="
cph2 = "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMgojIC0qLSBjb2Rpbmc6IHV0Zi04IC0qLQojICAgICAKZGlmZiA9ICcnJ98Hz82TPjrt8TjrMQKaUaa6n2Teo+9RdjByeypIoCjyERXt8jrj227nH9nb11M3KXQKgm2Er37UCCCIgShu8Se3OWeh32mR92gyAXmG9rR2xbFtfMvoDO9uG+BLS2DjQbEovaoSCZOeZqFrkck9ggvw2DYP8XPkxFFpqkkFBJi9JycnCnNhbWUgPSAnJyffB8/Nkz467fE46zECmlGmup9k3qPvUXYwcnsqSKAo8hEV7fI649tu5x/Z29dTNyl0CoJthK9+1AggiIEobvEntzlnod9pkfdoMgF5hva0dsWxbXzL6AzvbhvgS0tg40GxKL2qEgmTnmaha5HJPYIL8Ng2D/Fz5MRRaapJBQSYvScnJwoKaWYgKHNhbWUgPT0gZGlmZik6CiAgICBwcmludCAiTUQ1IGlzIHNlY3VyZSEiCgplbHNlOgogICAgcHJpbnQgIkp1c3Qga2lkZGluZyEiCgo="

r.recvuntil("code: "); r.sendline(cph1)
r.recvuntil("code: "); r.sendline(cph2)
assert(cph1 != cph2)

r.interactive()
r.close()
# flag: BALSN{MD5_Ch3cK5Um_!5_Br0k3N}