import socket

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("91.236.238.20", 9090)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((host, port))

name = input('Имя: ')

flag = True
join = False

while flag:
    if join == False:
        client.sendto(('[' + name + '] - присоединился к чату').encode('utf-8'), server)
        join = True
    else:
        message = input()
        if message != '':
            client.sendto(('[' + name + ']:' + message).encode('utf-8'), server)
        if message == 'выход':
            client.sendto(('[' + name + '] - покинул чат').encode('utf-8'), server)
            flag = False
client.close()






