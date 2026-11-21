import java.io.*;
import java.net.*;

public class Server {

    public static void main(String[] args) {

        int port = 6000;

        try {
            ServerSocket server = new ServerSocket(port);

            System.out.println("Server started...");
            System.out.println("Waiting for client...");

            Socket socket = server.accept();

            System.out.println("Client connected: "
                    + socket.getInetAddress());

            BufferedReader input = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));

            PrintWriter output = new PrintWriter(
                    socket.getOutputStream(), true);

            BufferedReader keyboard = new BufferedReader(
                    new InputStreamReader(System.in));

            String message;

            while (true) {

                message = input.readLine();

                if (message == null) {
                    break;
                }

                System.out.println("Client: " + message);

                if (message.equalsIgnoreCase("exit")) {
                    break;
                }

                System.out.print("Server reply: ");
                String reply = keyboard.readLine();

                output.println(reply);

                if (reply.equalsIgnoreCase("exit")) {
                    break;
                }
            }

            socket.close();
            server.close();

            System.out.println("Server disconnected.");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}