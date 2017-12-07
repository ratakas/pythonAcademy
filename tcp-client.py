import socket
target_host="127.0.0.1"
targeg_port=9999

#cerate sockte object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,targeg_port))

client.send(b"Abcd")

response= client.recv(4096)

print (response)

