import socket

alvo = '192.168.15.1'

for porta in range(1, 65535):

    client = socket.socket()
    client.settimeout(0.05)
    if client.connect_ex((alvo, porta)) == 0:
        print('Porta Aberta ==>', porta)