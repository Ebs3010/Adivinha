HANGMANPICS =['''
 o/ \o     
/|   |\   
/ \ / \ ''']


import socket

HOST = socket.gethostname()
PORT = 6041

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)

print HANGMANPICS[0]

print ("Welcome to the game Adivinhe!!")

#player_name = raw_input ("What is yor name?\n")
#print ("Hi %s !!" %(player_name) )  

print ("Tell me a number:\n")
msg = (raw_input())

while msg != '0':
    tcp.send (msg)
    print tcp.recv(1024)
    msg = (raw_input())

tcp.close()
    



    

