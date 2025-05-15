import socket
import os

# Configurações do servidor
HOST = 'localhost'
PORT = 8080

# Cria o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Servidor rodando em http://{HOST}:{PORT}")

def get_content_type(path):
    """Retorna o tipo MIME conforme a extensão do arquivo"""
    if path.endswith('.html'):
        return 'text/html; charset=UTF-8'
    elif path.endswith('.jpg') or path.endswith('.jpeg'):
        return 'image/jpeg'
    elif path.endswith('.mp4'):
        return 'video/mp4'
    else:
        return 'application/octet-stream'

while True:
    # Aceita conexão
    connection, addr = server_socket.accept()
    
    # Recebe a requisição HTTP
    try:
        request = connection.recv(1024).decode('utf-8', errors='ignore')
    except:
        connection.close()
        continue

    try:
        path = request.splitlines()[0].split()[1]
    except IndexError:
        connection.close()
        continue

    print(f"Requisição: {path} de {addr}")

    # Página inicial "/"
    if path == '/' or path == '/index.html':
        html = """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Servidor TCP - Sockets</title>
            <style>
                body {
                    font-family: 'Segoe UI', sans-serif;
                    background-color: #f5f5f5;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }
                header {
                    background-color: #007BFF;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }
                .container {
                    max-width: 800px;
                    margin: auto;
                    padding: 20px;
                    background: white;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    margin-top: 30px;
                    border-radius: 8px;
                }
                h2 {
                    color: #007BFF;
                }
                video {
                    width: 100%;
                    max-width: 640px;
                    height: auto;
                    display: block;
                    margin: 10px auto;
                    border-radius: 8px;
                }
                a.button {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #28a745;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                }
                a.button:hover {
                    background-color: #218838;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Projeto de Socket TCP</h1>
                <p>Exemplo de servidor web simples em Python</p>
            </header>

            <div class="container">
                <h2>🎥 Vídeo sobre Sockets</h2>
                <p>Assista ao vídeo abaixo para entender melhor como funcionam os sockets em redes.</p>
                <video controls>
                    <source src="/video.mp4" type="video/mp4">
                    Seu navegador não suporta vídeos.
                </video>

                <h2>📷 Visualizar Imagem</h2>
                <p>Clique no botão abaixo para ver uma imagem:</p>
                <a href="/imagem-page" class="button">Ver Imagem</a>
            </div>
        </body>
        </html>
        """

        header = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: {len(html)}
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: 0
Connection: close

"""

        connection.sendall(header.encode() + html.encode())

    # Página da imagem "/imagem-page"
    elif path == '/imagem-page':
        html = """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Visualizando Imagem</title>
            <style>
                body {
                    font-family: 'Segoe UI', sans-serif;
                    background-color: #f9f9f9;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                }
                header {
                    background-color: #dc3545;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }
                img {
                    max-width: 80%;
                    height: auto;
                    margin-top: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 15px rgba(0,0,0,0.2);
                }
                a.button {
                    display: inline-block;
                    margin-top: 30px;
                    padding: 10px 20px;
                    background-color: #007BFF;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                }
                a.button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Imagem Servida via Socket TCP</h1>
            </header>

            <img src="/imagem.jpg" alt="Imagem">

            <br>
            <a href="/" class="button">← Voltar à página inicial</a>
        </body>
        </html>
        """

        header = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: {len(html)}
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: 0
Connection: close

"""

        connection.sendall(header.encode() + html.encode())

    # Arquivo de vídeo ou imagem
    elif path in ['/video.mp4', '/imagem.jpg']:
        filepath = path[1:]  # Remove a barra inicial
        if not os.path.exists(filepath):
            response = "HTTP/1.1 404 Not Found\r\n\r\n Arquivo não encontrado."
            connection.send(response.encode())
        else:
            content_type = get_content_type(filepath)
            file_size = os.path.getsize(filepath)

            header = f"""HTTP/1.1 200 OK
Content-Type: {content_type}
Content-Length: {file_size}
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: 0
Connection: close

""".encode('utf-8')

            connection.sendall(header)

            with open(filepath, 'rb') as f:
                while True:
                    chunk = f.read(4096)  # Envia em blocos de 4KB
                    if not chunk:
                        break
                    connection.sendall(chunk)

    # Página não encontrada
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n Página não encontrada."
        connection.send(response.encode())

    connection.close()