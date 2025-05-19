import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class ClienteUDP {
    private static final String HOST = "localhost";
    private static final int PORT = 12345;
    private static final int NUM_PINGS = 10;
    private static final int TIMEOUT_MS = 1; // 1 segundo de timeout

    public static void main(String[] args) {
        try (DatagramSocket socket = new DatagramSocket()) {
            socket.setSoTimeout(TIMEOUT_MS);

            InetAddress address = InetAddress.getByName(HOST);

            for (int i = 1; i <= NUM_PINGS; i++) {
                String mensagem = "ping " + i;
                byte[] sendBuffer = mensagem.getBytes(StandardCharsets.UTF_8);
                DatagramPacket sendPacket = new DatagramPacket(
                    sendBuffer, sendBuffer.length, address, PORT
                );

                long startTime = System.currentTimeMillis();
                socket.send(sendPacket);
                System.out.print("Enviado: " + mensagem);

                try {
                    byte[] receiveBuffer = new byte[1024];
                    DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);

                    socket.receive(receivePacket);
                    long endTime = System.currentTimeMillis();

                    String resposta = new String(receivePacket.getData(), 0, receivePacket.getLength(), StandardCharsets.UTF_8);
                    long rtt = endTime - startTime;

                    System.out.println(" | Resposta: " + resposta + " | RTT: " + rtt + " ms");
                } catch (SocketTimeoutException e) {
                    System.out.println(" | Tempo esgotado.");
                }
            }
        } catch (IOException e) {
            System.err.println("Erro no cliente UDP: " + e.getMessage());
            e.printStackTrace();
        }
    }
}