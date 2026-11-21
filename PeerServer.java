import java.io.*;
import java.net.*;

public class PeerServer {

    public static void main(String[] args) {

        int port = 6001;
        String folderPath = "C:\\SharedFiles";

        try {
            ServerSocket server = new ServerSocket(port);

            System.out.println("Peer Server Started...");
            System.out.println("Waiting for client...");

            Socket socket = server.accept();

            System.out.println("Connected to: "
                    + socket.getInetAddress());

            File folder = new File(folderPath);

            File[] files = folder.listFiles(File::isFile);

            DataOutputStream output =
                    new DataOutputStream(socket.getOutputStream());

            if (files == null) {
                output.writeInt(-1);
            } else {
                output.writeInt(files.length);

                for (File file : files) {
                    output.writeUTF(file.getName());
                }
            }

            output.flush();

            System.out.println("File list sent successfully.");

            socket.close();
            server.close();

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}