import socket

server = ("localhost", 9090)  # адрес сервера
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9090))

name = input('Имя: ')  # вводим имя

flag = True

while flag:
    message = input()  # вводим сообщение
    if message != '':  # если сообщение не равно пустому символу
        client.sendall((f'[{name}]: + {message}').encode('utf-8'))
    if message == 'выход':  # если клиент хочет выйти из чата
        client.sendall((f'[{name}] - покинул чат').encode('utf-8'))
        flag = False
client.close()
