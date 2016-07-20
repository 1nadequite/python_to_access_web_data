# connect to web server
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # opened connection
mysock.connect( ('www.py4inf.com', 80) ) # host, port

mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n') # request (hit enter twice)

while True:  # read response
    data = mysock.recv(512) # receive ut to 512 characters at a time
    if (len(data) < 1):
        break
    print data

mysock.close() # close socket


