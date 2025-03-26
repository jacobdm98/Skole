from socket import *

clientsocket = socket(AF_INET, SOCK_STREAM)

sName = "127.0.0.1"
sPort = 8080

clientsocket.connect((sName, sPort))

while True:
    regn = input("Skriv regne stykke: ")

    clientsocket.send(regn.encode())


    if regn == "slut":
        break

    data = clientsocket.recv(1024)

    print("from server: ", data.decode())

    
clientsocket.close()