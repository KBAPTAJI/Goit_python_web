import socket
from threading import Thread


def server(host, port):
    with socket.socket() as sock:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((host, port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_name = sock.getsockname()
        print(f'Socket opening with {sock_name}')
        while True:
            data, addres = sock.recvfrom(1024)
            if not data:
                break
            print(data)
            print(addres)


def main():
    host = '127.0.0.1'
    port = 5000
    server(host, port)
    serv = Thread(target=server, args=(host, port))
    serv.start()
    serv.join()


if __name__ == '__main__':
    main()
