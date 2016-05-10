HANGMANPICS =['''
 o/ \o     
/|   |\   
/ \ / \ ''']


import socket

HOST = socket.gethostname()
PORT = 6093

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
msg = (raw_input())

while msg != '0' :
    tcp.send (msg)
    print tcp.recv(1024)
    msg = (raw_input())    
    bids = bids + 1
    print("Bids %d/5 \n" %(bids))
    if bids == 5:
        msg = '0'
        print("You Lose!!\n")


tcp.close()
    



    

