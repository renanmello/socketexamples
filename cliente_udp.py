import socket
import time

# Configurações do servidor
SERVER_IP = 'localhost'
SERVER_PORT = 12345
ADDR = (SERVER_IP, SERVER_PORT)

# Tempo máximo de resposta em milissegundos
RTT_TIMEOUT_MS = 5  # Se o RTT for maior que isso, consideramos como "perda de pacote"

# Cria socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)  # Timeout total para resposta (opcional)

print(f"Enviando pings para {ADDR} com limite de RTT de {RTT_TIMEOUT_MS} ms:\n")

for i in range(1, 11):  # Envia 10 pings
    message = f"PING {i}".encode()
    start_time = time.time()

    try:
        client_socket.sendto(message, ADDR)
        data, server = client_socket.recvfrom(1024)
        end_time = time.time()
        
        rtt_ms = round((end_time - start_time) * 1000, 2)  # Converte para ms

        if rtt_ms > RTT_TIMEOUT_MS:
            print(f"Pacote {i} demorou {rtt_ms} ms → considerado como perdido.")
        else:
            print(f"Resposta de {ADDR}: {data.decode()} | RTT: {rtt_ms} ms")

    except socket.timeout:
        print("Solicitação expirada.")

client_socket.close()