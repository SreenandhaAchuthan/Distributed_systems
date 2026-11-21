import java.io.*;
import java.net.*;

public class Client {

    public static void main(String[] args) {

        String serverIP = "11.12.2.108";
        int port = 6000;

        try {
            Socket socket = new Socket(serverIP, port);

            System.out.println("Connected to server.");

            BufferedReader input = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));

            PrintWriter output = new PrintWriter(
                    socket.getOutputStream(), true);

            BufferedReader keyboard = new BufferedReader(
                    new InputStreamReader(System.in));

            String message;

            while (true) {

                System.out.print("Client message: ");
                message = keyboard.readLine();

                output.println(message);

                if (message.equalsIgnoreCase("exit")) {
                    break;
                }

                String reply = input.readLine();

                System.out.println("Server: " + reply);

                if (reply == null ||
                        reply.equalsIgnoreCase("exit")) {
                    break;
                }
            }

            socket.close();

            System.out.println("Client disconnected.");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}