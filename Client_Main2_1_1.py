HANGMANPICS =['''
 o/ \o     
/|   |\   
/ \ / \ ''']

HANGMANPICS1 =['''
    _  _  _  _
|  | ||_ |_ |_|
|_ |_| _||_ | \ ''']

HANGMANPICS2 =['''
                   _  _
\   / | |\ | |\ | |_ |_|
 \|/  | | \| | \| |_ | \ ''']

import socket

HOST = socket.gethostname()
PORT = 6102

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)

print HANGMANPICS[0]

print ("Welcome to the game Adivinhe!!\n")
print "Try to guess the number between 1 and 50:\n"

#player_name = raw_input ("What is yor name?\n")
#print ("Hi %s !!" %(player_name) )

bids = 1

print ("Tell me a number:\n")
#msg = (raw_input())
msg = '50'

while msg != '0' :
    msg = (raw_input())
    tcp.send (msg)
    data = tcp.recv(1024)
    
    bids = bids + 1
    
    if data != '0' and bids!=5:
        print data
        print("Bid %d/5 \n" %(bids))
    
    
    if bids == 5:
        msg = '0'
        print HANGMANPICS1[0]

    elif data == '0':
        msg = '0'
        print HANGMANPICS2[0]


 
tcp.close()
    



    

