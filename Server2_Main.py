
import socket
import random
import thread

HOST = socket.gethostname()
PORT = 6072

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))

print ("Socket criado com sucesso!!\n")

#Numeros de conexoes permitidas
tcp.listen(2)


#Funcao para tratar multiplas conexoes
def clientthread(con, client):
        print ("New connection", client)
        while True:
                try:
                        guess(con)
                        
                except ValueError:
                        print ("Finished conection.", client)
                        con.close()
                        thread.exit()

                        
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
    thread.start_new_thread(clientthread, tuple([con, client]))

print ("Finished conection.", client)
tcp.close()  
        




        
        
        









