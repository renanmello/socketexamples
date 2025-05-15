# 🧪 Projeto de Estudo: Comunicação via Sockets em Python

Projeto desenvolvido durante a pós-graduação com objetivo de compreender na prática o funcionamento da comunicação entre cliente e servidor utilizando **Sockets em Python**, abordando protocolos **TCP (confiável)** e **UDP (não confiável)**.
## 📌 Objetivo 

Demonstrar o uso básico de sockets para: 

    Criar um servidor Web simples usando TCP (protocolo confiável) 
    Implementar um cliente "ping" usando UDP (protocolo não confiável) 
    Medir latência (RTT - Round Trip Time)
    Simular perda de pacotes em redes não confiáveis
     

## 🧩 Funcionalidades 

## 🔹 Servidor TCP (servidor_tcp.py) 
```
    Servidor HTTP que responde requisições de navegadores
    Serve páginas HTML com vídeo embutido e imagem
    Estilizado com CSS interno
    Suporta navegação entre páginas (ex: página inicial → página da imagem)
```     

## 🔹 Cliente UDP (cliente_udp.py) 
```
    Envia 10 mensagens "ping" ao servidor UDP
    Mede o tempo de resposta (RTT)
    Trata timeout caso não haja resposta em até 1 segundo
    Pode ser configurado para ignorar respostas lentas (ex: RTT > 5ms)
```     

## 🔹 Servidor UDP (servidor_udp.py) 
```
    Responde às mensagens "ping" com "pong"
    Pode simular perda de pacote com probabilidade ajustável
 ```    

## 🗂️ Estrutura do Projeto
```
projeto-sockets-tcp-udp/
├── servidor_tcp.py       # Servidor Web com socket TCP
├── servidor_udp.py       # Servidor de "pong" com socket UDP
├── cliente_udp.py        # Cliente de "ping" com medição de RTT
├── video.mp4             # Arquivo de vídeo usado no servidor TCP
├── imagem.jpg            # Imagem usada no servidor TCP
└── README.md             # Este arquivo
```
## ▶️ Como Executar 
1. Requisitos 

    - Python 3.7 ou superior
    - Navegador web (Firefox, Chrome, etc.)
  

2. Passo a passo 
🔸 Servidor TCP (Web)
```
python servidor_tcp.py
```
 

Acesse no navegador:

👉 http://localhost:8080

🔸 Servidor UDP 
```
python servidor_udp.py
``` 
 
- Fica escutando por pings na porta 12345.
   
🔸 Cliente UDP 
```
python cliente_udp.py
```
- Envia 10 pings ao servidor e mostra RTT ou timeout. 

## 📚 Aprendizados

Este projeto visa demonstrar conceitos importantes de redes e programação com sockets, incluindo:

| Conceito              | Aplicação                                               |
|-----------------------|----------------------------------------------------------|
| TCP                   | Comunicação confiável, orientada a conexão              |
| UDP                   | Comunicação rápida, sem garantias                        |
| Socket                | Interface de programação para comunicação de rede        |
| RTT (Round Trip Time) | Tempo de ida e volta de uma mensagem                     |
| Timeout               | Tratamento de falhas em redes não confiáveis             |
 
💼 Autores 
{Renan Mello, 
Amanda Machado, 
Rodolfo Cruz}

🎓 Pós-Graduação em Ciência da Computação Universidade Federal do Pará

📬 Contato 

E-mail: mellorenan19@gmail.com

LinkedIn: https://www.linkedin.com/in/renan-mello-202ba5211

📚 Referências 

    Documentação oficial do módulo socket  do Python
    Livro: Computer Networking: A Top-Down Approach  – James F. Kurose e Keith W. Ross
     

🙌 Agradecimentos 

Agradeço à instituição de ensino pela oportunidade de aprendizado e aos professores pelo conteúdo teórico base para este projeto prático. 

🏁 Conclusão 

Este projeto é uma excelente introdução prática ao mundo das redes de computadores, mostrando como aplicar conceitos teóricos em código real com linguagem Python. 
