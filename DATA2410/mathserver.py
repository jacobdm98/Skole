from socket import*
import _thread as thread

def handle(connection, adress):
    try:
        while True:
            data = connection.recv(1024).decode()

            if data == "slut":
                break

            mat = data.split()
            if mat[1] == "+":
                res = int(mat[0]) + int(mat[2])

            elif mat[1] == "-":
                res = int(mat[0]) - int(mat[2])

            else:
                res = "fejl"


            connection.send(str(res).encode())


    except:
        connection.send("fejl".encode())

        
    finally:
        print("connection terminated: ", adress)
        connection.close()


serverSocket = socket(AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 8080

serverSocket.bind((host, port))
serverSocket.listen(5)
print("server is listening")

while True:
    connection, adress = serverSocket.accept()
    print("new connecetion from ", adress)

    thread.start_new_thread(handle, (connection, adress))

serverSocket.close()