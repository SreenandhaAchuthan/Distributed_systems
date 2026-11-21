import java.io.*;
import java.net.*;

public class PeerClient {
    public static void main(String[] args) {
        String serverIP = "11.12.2.108";
        int port = 6001;
        try {
            Socket socket = new Socket(serverIP, port);
            System.out.println("Connected to Peer Server.");
            DataInputStream input =
                    new DataInputStream(socket.getInputStream());
            int count = input.readInt();
            System.out.println("\nFiles available in shared folder:");
            if (count == -1) {
                System.out.println("Folder not found.");
            } else if (count == 0) {
                System.out.println("No files available.");
            } else {
                for (int i = 0; i < count; i++) {
                    String fileName = input.readUTF();
                    System.out.println(fileName);
                }
            }
            socket.close();
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}