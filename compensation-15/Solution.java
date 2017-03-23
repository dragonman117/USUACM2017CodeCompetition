import java.util.*;
import java.io.*;

class Solution {
    public static void main (String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int weeks = sc.nextInt();
        double hourlyRate = sc.nextDouble();
        double compensation = 0.0;
        for (int i = 0; i < weeks; i++) {
            int weekdayHours = 0;
            int weekendHours = 0;
            for (int weekDay = 1; weekDay <= 5; weekDay++)
                weekdayHours += sc.nextInt();
            for (int weekDay = 6; weekDay <= 7; weekDay++)
                weekendHours += sc.nextInt();
            if (weekdayHours <= 40)
                compensation += weekdayHours * hourlyRate;
            else
                compensation += 40 * hourlyRate + (weekdayHours - 40) * (1.5 * hourlyRate);
            compensation += weekendHours * (1.5 * hourlyRate);
        }
        System.out.println(String.format("%.2f", compensation));
    }
}
