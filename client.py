import socket  #client
import os
import time

TCP_IP = "127.0.0.1"           #(input('ip')) #"127.0.0.1"
TCP_PORT = 22280
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def conn():
    print ("Sending server request...")
    try:
        s.connect((TCP_IP, TCP_PORT))
        print ("Connection sucessful")
    except:
        print ("Connection unsucessful. Make sure the server is online.")



def upld(file_name):
    print (f'\nUploading file: {file_name}')
    
    s.send(file_name.split("/")[-1].encode()) 
    
    try:        
        with open(file_name, "rb") as content:
            name_upld = content.read()
            print(name_upld)
            

    except:
            print ("Couldn't open file. Make sure the file name was entered correctly.")
            return 
    try:
            s.sendall((file_name.split("/")[-1]).encode())
            time.sleep(1)
            s.sendall(name_upld)
            time.sleep(1)
            s.sendall(b"@@@end@@@")
    except:
            print ("Couldn't make server request. Make sure a connection has bene established.")
            return 
        


def dwld(file_name):
    name_1 = (file_name.split("/")[-1])
    while True:
        print("ok")
        s.send(file_name.encode())
        file = open(name_1, "wb")
        finished = False
        while not finished:
            data = s.recv(1024)
            file.write(data)
            if data == b"@@@end@@@":
                finished = True
                file.close()
                s.close()
                print("\n Server closed the connection \n")
                return


def list_dir():
    print(s.recv(1024))    
    return


def close():
    s.close
    return



def main():
    
    #n = int(input('Please enter the number of iterations:'))

    for i in range(0,7777):

        print('If you want to connect, Enter 1 for choice 1\n')

        print('If you want to upload, Enter 2 for choice 2\n')

        print('If you want to do downloads, Enter 3 for choice 3\n')

        print('If you want to see the list of files on the server, Enter 4 for choice 4\n')

        print('Enter the close 5\n')

        choice = int(input('Enter your choice:'))

        if (choice == 1):
            conn()
        
        elif (choice == 2):
            s.sendall(b"upld")
            file_name = input('send the link!...')
            upld(file_name)
            

        elif (choice == 3): 
            s.sendall(b"dwld")
            file_name = input('send the link!...')
            dwld(file_name)
            

        elif (choice == 4):

            s.sendall(b"list_dir")
            list_dir()

        elif (choice == 5):
            close()
            s.sendall(b"close")

        else:
            print('Invalid choice')

if __name__ == "__main__":
    main()
