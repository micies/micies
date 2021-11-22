import socket



# Initialise socket stuff
TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 12345 # Just a random choice
BUFFER_SIZE = 1024 # Standard chioce
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file_name = input('send the link!...')
def conn():
    print ("Sending server request...")
    try:
        s.connect((TCP_IP, TCP_PORT))
        s.sendall(b'hi')
        print ("Connection sucessful")
    except:
        print ("Connection unsucessful. Make sure the server is online.")



def upld(file_name):
    print (f'\nUploading file: {file_name}')
    try:
        with open(file_name, "rb") as content:
            aaa = content.read()
            print(aaa)
    except:
        print ("Couldn't open file. Make sure the file name was entered correctly.")
        return
    try:
        s.send(aaa)
    except:
        print ("Couldn't make server request. Make sure a connection has bene established.")
        return
    try:
        s.recv(BUFFER_SIZE)
    except:
        print ("Error sending file details")

conn()
upld(file_name)

