import socket, time, json
from data import SERVER, PORT
from auth import auth

server = (SERVER, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER, 0))
print(f'Установлено соединение с сервером: {sock.getsockname()[0]} {sock.getsockname()[1]} ')


while True:
    name = input('Введите имя: ')
    password = input('Введите пароль: ')

    if auth(name, password):
        break


while True:
    try:
        message = (f'Пользователь {name}: отправил сообщение ' + str(input('Введите сообщение: '))).encode()
        sock.sendto(message, server)
        if message.decode('UTF-8').split(':')[1].strip().split(' ')[2] == 'q':
            raise Exception
        print(f'Данные "{message.decode()}" на сервер ')
        data, addr = sock.recvfrom(1024)
        print(f'Данные "{data.decode()}" получены от сервера')
    except Exception:
        print(f'Соединение с сервером {SERVER} {PORT} разорвано')
        break
    except KeyboardInterrupt:
        print(f'Соединение с сервером {SERVER} {PORT} разорвано некорректно. Для корректного выхода введите "q"')
        break
    time.sleep(2)
sock.close()
