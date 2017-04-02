import java.util.*;
import java.io.*;

class Solution {
    public static void main (String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        Set<String> dictionary = new HashSet<>();
        for (int i = 0; i < n; i++)
            dictionary.add(sc.next());

        while (k-- > 0) {
            String wordToCheck = sc.next();
            List<String> suggestions = new ArrayList<>();
            if (!dictionary.contains(wordToCheck)) {
                for (String dictWord : dictionary) {
                    if (distance(wordToCheck, dictWord) <= 2)
                        suggestions.add(dictWord);
                }
            }
            if (dictionary.contains(wordToCheck)) {
                System.out.println("CORRECT");
            }
            else if (suggestions.size() == 1) {
                System.out.println("YES " + suggestions.get(0));
            }
            else {
                Collections.sort(suggestions);
                StringBuffer s = new StringBuffer("NO");
                for (String word : suggestions)
                    s.append(' ').append(word);
                System.out.println(s.toString());
            }
        }
    }
    private static int distance(String word1, String word2) {
        int[][] D = new int[word1.length() + 1][word2.length() + 1];
        for (int i = 0; i <= word1.length(); i++)
            D[i][0] = i;
        for (int j = 0; j <= word2.length(); j++)
            D[0][j] = j;
        for (int i = 1; i <= word1.length(); i++) {
            for (int j = 1; j <= word2.length(); j++) {
                char ch1 = word1.charAt(i - 1);
                char ch2 = word2.charAt(j - 1);
                int replaceCost = (ch1 == ch2) ? 0 : 1;
                D[i][j] = Math.min(D[i-1][j] + 1, Math.min(D[i][j-1] + 1, D[i-1][j-1] + replaceCost));
            }
        }
        return D[word1.length()][word2.length()];
    }
}
