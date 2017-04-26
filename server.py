#! /usr/bin/env python
import socket
host = ''
port = 50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
conn,addr= s.accept()

print 'got  connection big brother',addr
while 1:
    data =conn.recv(4096)
    if not data:break
    conn.sendall(data.upper())
conn.close()
