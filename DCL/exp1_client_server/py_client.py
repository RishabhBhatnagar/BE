import socket
import sys


# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()

try: # EAFP
    port = int(sys.argv[1])
except:
    print("No valid port number given via cli, exitting....")
    exit(1)

# connecting with the listening server.
s.connect((host, port))

# Receive no more than 1024 bytes
while True:
    num_str = input(">>> ")
    if num_str.isdigit(): # LBYL
        print("sending dat")
        # sending the number to the server.
        s.send(num_str.encode('utf8'))
        print('sent')
        # receiving the data from server.
        print('receiving')
        print(s.recv(1024))
        print('wait for server to reply back')
s.close()
print (msg.decode('ascii'))
