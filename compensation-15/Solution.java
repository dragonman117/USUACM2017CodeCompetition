import java.util.*;
import java.io.*;

class Solution {
    public static void main (String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        int weeks = in.nextInt();
        double hourlyRate = in.nextDouble();
        double compensation = 0.0;
        for (int i = 0; i < weeks; i++) {
            int weekHours = 0;
            for (int weekDay = 0; weekDay < 7; weekDay++)
                weekHours += in.nextInt();
            if (weekHours <= 40) {
                compensation += weekHours * hourlyRate;
            }
            else {
                compensation += 40 * hourlyRate;
                compensation += (weekHours - 40) * (1.5 * hourlyRate);
            }
        }
        System.out.println(String.format("%.2f", compensation));
    }
}
