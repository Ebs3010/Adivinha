
import socket
import random
from thread import *
import sys

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 6031
tcp.bind((HOST, PORT))

print ("Socket criado com sucesso!!\n")

#Numeros de conexoes permitidas
tcp.listen(2)

#
def clientthread(con):
        while True:
            guess(con)
        #con.send("Congratulations!!")

        #con.close

#As comparacoes sao feitas dentro desta funcao
def guess (con):
    jog1_number = int(con.recv(1024))
    
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
            
    con.close    
      

#O servidor gera um numero aleatorio entre 1 e 60
number = random.randint(1, 60)

while True:
    con, client = tcp.accept()
    print("Good job!", client)
    print ("Number", number)       
    
    print "Try to guess the number between 1 and 60:"
    
    start_new_thread(clientthread, (con,))

print ("Finished conection.", client)
con.close()
tcp.close()  
        




        
        
        









