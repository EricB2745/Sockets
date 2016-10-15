import socket
import sys

class Socket(object):

    def __init__(self, host):
        print 'initializing socket'
        self.host = host
        self.create_socket()
    
    def create_socket(self):
        print 'trying to create socket'
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
            sys.exit();

        print 'Socket Created'


        try:
            remote_ip = socket.gethostbyname( self.host )
            print remote_ip

        except socket.gaierror:
            #could not resolve
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
	
	
s = Socket('www.google.com')
