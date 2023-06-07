import socket

host = socket.gethostbyname(socket.gethostname())         #узнаем наш IP
port = 0                        #наш порт

server = ("91.236.238.20", 9090)      #адрес сервера

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((host, port))   #привязываем адрес к сокету

name = input('Имя: ')       #вводим имя

flag = True
join = False

while flag:
    if join == False:       #если клиент не присоединен
        client.sendto(('[' + name + '] - присоединился к чату').encode('utf-8'), server) #
        join = True
    else:
        message = input()    #вводим сообщение
        if message != '':          #если сообщение не равно пустому символу
            client.sendto(('[' + name + ']:' + message).encode('utf-8'), server)
        if message == 'выход':       #если клиент хочет выйти из чата
            client.sendto(('[' + name + '] - покинул чат').encode('utf-8'), server)
            flag = False
client.close()






