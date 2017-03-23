import java.util.*;
import java.io.*;

class Solution {
    public static void main (String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String message = sc.next();
        StringBuffer encodedMsg = new StringBuffer();
        char runChar = message.charAt(0);
        int runLength = 0;
        for (int i = 0; i < message.length(); i++) {
            char ch = message.charAt(i);
            if (ch == runChar) {
                runLength++;
            }
            else {
                encodedMsg.append(runLength).append(runChar);
                runChar = ch;
                runLength = 1;
            }
        }
        encodedMsg.append(runLength).append(runChar);
        if (encodedMsg.length() < message.length())
            System.out.println("YES " + encodedMsg);
        else
            System.out.println("NO");
    }
}
