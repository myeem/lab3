import socket
from data import SERVER, PORT

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    try:
        socket.bind((SERVER, 80))
    except PermissionError:
        socket.bind((SERVER, PORT))
        break
print('Сервер запущен')
print(f'порт: {PORT} - прослушивается')


def server():
    while True:
        data, addr = socket.recvfrom(1024)
        print(f'Клиент подключился:  {addr}')
        client = f'ip {addr[0]} port {addr[1]}'
        if data.decode('UTF-8') == 'q':
            print(f'Клиент {client} - отключился')
            break
        if not data:
            break
        socket.sendto(data.upper(), addr)
        print(f'Данные "{data.decode("UTF-8")}" были отправлены клиенту - {client}')

    print('Сервер отключился')


server()
