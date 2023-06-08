import socket

server = ("localhost", 9090)  # адрес сервера
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12953))

name = input('Имя: ')  # вводим имя

flag = True

while flag:
    message = input()  # вводим сообщение
    if message != '':  # если сообщение не равно пустому символу
        client.sendto(('[' + name + ']:' + message).encode('utf-8'), server)
    if message == 'выход':  # если клиент хочет выйти из чата
        client.sendto(('[' + name + '] - покинул чат').encode('utf-8'), server)
        flag = False
client.close()
