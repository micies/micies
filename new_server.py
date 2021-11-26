import socket
import os
import time


s = socket.socket()

PORT = 22280
print("\n Server is listing on port :", PORT, "\n")

s.bind(('', PORT))

s.listen()
conn, addr = s.accept() 



def upld():
    try:
        a = conn.recv(1024).decode()
   # if "@" in a:
    #    print("a.split")
     #   a = a.split("@")[0]
   # else:
    #    print("name not completed!")
     #   return
        print("with open a, wb as file_2")
        conn.close()
        file_2 = open (a, "wb")
        print('a')
        finished = False
        while not finished:
            RecvData = conn.recv(1024)
            file_2.write(RecvData)
            if RecvData == b"@@@end@@@":
                print("finishing...")
                finished = True
                file_2.close()
                print("closing socket")
                conn.close()
                return
    except Exception as e:
        pass

    
    print("\n File has been copied successfully \n")
    
    print("\n Server closed the connection \n")
    return 

def dwld(file_name):
    try:
        with open(file_name, "rb") as content:
            read_down = content.read()
            print(read_down)
    except:
        print ("Couldn't open file. Make sure the file name was entered correctly.")
        return
    try: 
        conn.sendall(read_down)
        time.sleep(1)
        conn.sendall(b"@@@end@@@")
        print("ok")
        conn.close()
    except:
        print ("Couldn't make server request. Make sure a connection has bene established.")
        return

def close():
    conn.close
    return

def list_dir():
    arr = str(os.listdir())
    conn.sendall(arr.encode())
    return

    
def main():

    while True:
        #print ("\n\nWaiting for instruction")
        data = conn.recv(1024).decode()
        
        #print ("\nRecieved instruction: {}".format(data))
        if data == "list_dir":
            list_dir()

        elif data == "dwld":
            resv_down= conn.recv(1024).decode()
            name_down = (resv_down.split("/")[-1])
            dwld(resv_down)
        elif data == "upld":
            upld()
        elif data == "close":
            close()
        data = None

if __name__ == "__main__":
    main()
