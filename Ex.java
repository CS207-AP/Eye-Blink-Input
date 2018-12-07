import javax.swing.*;
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
   
   
   JFrame f = new JFrame("Label Example");
   JLabel[][] labels;
   f.setSize(800, 800);

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
   String str = "Text Entered: ";

   int x = 100, y = 100;
   labels = new JLabel[6][7];
   for (int i = 0; i < 6; i++) {
    for (int j = 0; j < 7; ++j) {
     labels[i][j] = new JLabel(c[i][j]);
     labels[i][j].setOpaque(true);
     labels[i][j].setBounds(x * (j + 1), y * (i + 1), 50, 50);
     f.add(labels[i][j]);
    }
   }

   JLabel txt = new JLabel(str);
   txt.setOpaque(true);
   txt.setBounds(20, 0, 200, 50);
   f.add(txt);

   f.setLayout(null);
   f.setVisible(true);
   int closed, opened, closedin, openedin, k;
   long n1;
  }
 }
}
