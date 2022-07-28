import socket
from threading import Thread


def client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((host, port))
        while True:
            mess = input('')
            sock.sendall(mess.encode())
            if mess == 'bye':
                break


def main():
    host = '127.0.0.1'
    port = 5000
    cli = Thread(target=client, args=(host, port))
    cli.start()


if __name__ == '__main__':
    main()
