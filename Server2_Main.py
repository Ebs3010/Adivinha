
import socket
import random
from thread import *

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 6047
tcp.bind((HOST, PORT))

print ("Socket criado com sucesso!!\n")

#Numeros de conexoes permitidas
tcp.listen(2)

#
def clientthread(con):
        print ("New connection")
        while True:
                try:
                        guess(con)
                        
                except ValueError:
                        print ("Finished conection.", client)
                        con.close()
                        return 0

#As comparacoes sao feitas dentro desta funcao
def guess (con):
    jog1_number = int(con.recv(1024))
    
    if jog1_number == number:  
        con.send("Congratulations!!")

    else:        
        if(jog1_number > number):
            con.send("Try a small number")

        else:
            con.send("Try a big number")        
      

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
        




        
        
        









