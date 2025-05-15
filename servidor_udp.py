import socket

# Configuração do servidor UDP
HOST = 'localhost'
PORT = 12345

# Cria o socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Servidor UDP ouvindo em {HOST}:{PORT}")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Mensagem recebida de {addr}: {data.decode()}")
    server_socket.sendto(f"pong {data.decode()}".encode(), addr)