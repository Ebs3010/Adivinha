
import socket
import random

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 6008
tcp.bind((HOST, PORT))

tcp.listen(2)

#As comparacoes sao feitas dentro desta funcao
def guess ():
    jog1_number = int (con.recv(1024))
    
    if jog1_number == number:  
        #print("Congratulations!!")
        con.send("Congratulations!!")
        return 0
        
    else:        
        if(jog1_number > number):
            #print("Try a small number")
            con.send("Try a small number")

        else:
            #print("Try a big number")
            con.send("Try a big number")        
      

#O servidor gera um numero aleatorio entre 1 e 60
number = random.randint(1, 60)

while True:
    con, client = tcp.accept()
    print("Good job!", client)
    print ("Number", number)
    
    print "Try to guess the number between 1 and 60:"
    while True:        
        guess()

    print ("Finished conection.", client)
    con.close()  
        




        
        
        









