import socket  
import signal  # Shutdown
import time    # Current time

class Server:
 

 def __init__(self, port = 8080):
     
     self.host = ''   
     self.port = port
     

 def startserver(self):
     
     self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     try: 
         
         self.socket.bind((self.host, self.port))
         

     except Exception as e:
         print ("Could not aquire port:",self.port,"\n")
         self.shutdown()
         import sys
         sys.exit(1)
        
         

     print ("Connection established with port ", self.port)
     print ("Press Ctrl+C to shut down the server and exit.")
     self.connect()
     

 def shutdown(self):
     
    print("Shutting down the server")
    self.socket.shutdown(socket.SHUT_RDWR)
         

    
 

 def connect(self):
     self.socket.listen(3)
     
     while True:
         
          

         xyz, abcd = self.socket.accept()
         x='HTTP/1.1 200 OK\nContent-Type: text/html\n'
         x+=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
         
         xyz.send(x)
         xyz.send('\n')
         xyz.send('Hi!')
         
         

         

def graceful_shutdown(sig, dummy):
    """ This function shuts down the server. It's triggered
    by SIGINT signal """
    s.shutdown() #shut down the server
    import sys
    sys.exit(1)

###########################################################
# shut down on ctrl+c
signal.signal(signal.SIGINT, graceful_shutdown)

print ("Starting web server")
s = Server(1234)  # construct server object
s.startserver() # aquire the socket

