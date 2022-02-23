

import socket
Ports = [21,22,25,3306]
for i in range (0,4):
    s = socket.socket()
    
    Ports = Ports[i]
    print ("This Is the Banner for the Port")
    print (Ports)

    s.connect (("192.168.1.101", Ports))
    answer = s.recv (1024)
    print (answer)
    s.close ()
