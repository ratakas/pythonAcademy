import sys
import socket
import getopt
import threading
import subprocess

#gloabal variables

listen = False
command = False
upload = False
execute = ""
target = ""
port = 0
upload_destination = ""

def usage():
	print ("BHP Net Tool")
	print 
	print ("Usage: bhpnet.py -t target_host -p port")
	print ("-l --listen - listen on [host]:[port] forincoming connections")
	print ("-e --execute=file_to_run - execute the given file uponreceiving a connection")
	print ("-c --command - initialize a command shell")
	print ("-u --upload=destination - upon receiving connection upload a file and write to [destination]")

	print 
	print 
	print ("Examples: ")
	print ("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
	print ("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
	print ("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
	print ("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")
	sys.exit(0)


def main():
	global listen
	global command
	global upload
	global execute
	global target
	global port
	global upload_destination
	
	if not len(sys.argv[1:]):
		usage()
	try:
		opts,arg=getopt.getopt(sys.argv[1:], "hle:t:p:cu", ["help","target","port","command","upload"])
		print(arg)
		print(opts)
	except getopt.GetoptError as e:
		print(e)
		usage()

	for o,a in opts:
		if o in ( "-h", "--help"):
			usage()
		elif o in ("-l", "--listen"):
			listen=True
		elif o in ("-e", "--execute"):
			execute=a
		elif o in ("-c", "--commandshell"):
			command=True
		elif o in ("-u", "--upload"):
			upload=a
		elif o in ("-t", "--target"):
			target=a
		elif o in ("-p", "--port"):
			port= int(a)
		else:
			print("pailas options")

	print("listen: "+ str(listen))
	print("execute: "+ str(execute))
	print("commandshell: "+str(command))
	print("upload: "+str(upload))
	print("target: "+str(target))
	print("port: "+ str(port))

	if not listen and len(target) and port > 0:
		#buffer= sys.stdin.read()
		#client_sender(buffer)
		print("pasa")
		print("ggit")

def client_sender(buffer):
	
	client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	try:
		client.connect((target,port))
		if len(buffer):
			client.send(buffer)

		while True:
			recv_len=1
			response=""
			while recv_len:
				data= client.recv(4096)
				recv_len= len(data)
				response+=data

				if recv_len < 4096:
					break
			print (response)
			buffer= raw_input("")
			buffer+="\n"
			client.send(buffer)
	except Exception as e:
		print("eeror exiting..")
		print(e)
		client.close()


if __name__ == '__main__':
	main()