# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('utf-8')

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE =  raw_input("Plz input:")

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
sock.close()