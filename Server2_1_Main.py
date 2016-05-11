
import socket
import random
import thread

HOST = socket.gethostname()
PORT = 6102

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))

print ("Socket created!!")

#Numeros de conexoes permitidas
tcp.listen(2)

#Funcao para tratar multiplas conexoes
def clientthread(con, client):
        #print ("New connection\n", client)
        while True:
                guess(client)
                
        print 'Finished! ', client
        con.close()
        thread.exit()
        
                        
#As comparacoes sao feitas dentro desta funcao
def guess (client):
    jog1_number = int(con.recv(1024))
    
    if jog1_number == number:
            con.send('0')

    else:        
        if(jog1_number > number):
            con.send("Try a small number")

        else:
            con.send("Try a big number")        
      

#O servidor gera um numero aleatorio entre 1 e 50
number = random.randint(1, 50)

#Loop necessario para o servidor ficar esperando por clientes.
while True:
        print("Wainting for conection:\n")
        con, client = tcp.accept()
        print("Good job!", client)
                
        print ("Number: ", number)       
        thread.start_new_thread(clientthread, tuple([con, client]))

print ("Finished conection.\n", client)
tcp.close()  
        




        
        
        









