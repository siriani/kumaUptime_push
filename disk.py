import requests
import shutil

url = 'https://status.dicas.link/api/push/llrRxgUPFP?status=up&msg=98%&ping='

total, used, free = shutil.disk_usage("/")

total = (total // (2**30))
used = (used // (2**30))
free = (free // (2**30))
if free < 10:
    url = 'https://status.dicas.link/api/push/llrRxgUPFP?status=down&msg='+str(free)+'GB&ping='
    x = requests.get(url)
else:
    url = 'https://status.dicas.link/api/push/llrRxgUPFP?status=up&msg='+str(free)+'GB&ping='
    x = requests.get(url)

