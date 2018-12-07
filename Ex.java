import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

class Ex {
 public static void main(String args[]) throws Exception {
  {
   String fromClient;
   ServerSocket server = new ServerSocket(8960);
   Socket client = server.accept();
   BufferedReader inFromClient = new BufferedReader(new InputStreamReader(client.getInputStream()));

     String c[][] = {
    {
     "END",
     "E",
     "K",
     "Q",
     "W",
     "3",
     "9"
    },
    {
     "SPACE",
     "F",
     "L",
     "R",
     "X",
     "4",
     "0"
    },
    {
     "A",
     "G",
     "M",
     "S",
     "Y",
     "5",
     ""
    },
    {
     "B",
     "H",
     "N",
     "T",
     "Z",
     "6",
     ""
    },
    {
     "C",
     "I",
     "O",
     "U",
     "1",
     "7",
     ""
    },
    {
     "D",
     "J",
     "P",
     "V",
     "2",
     "8",
     ""
    }
   };
  }
 }
}
