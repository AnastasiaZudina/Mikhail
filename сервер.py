import socket
def connect():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('',9090))
    server.listen(0)
    connection, address=server.accept()   
    print('Подключен клиент.')
    while True:
        text=input('Введите текст: ')
        try:
            connection.send((text).encode('utf-8'))
        except ConnectionResetError:
            print('Нет подключенных клиентов')
            server.close()
            connect()
connect()
