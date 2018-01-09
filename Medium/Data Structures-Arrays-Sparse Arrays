import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        
        int n = s.nextInt();
        String[] lines = new String[n];
        for (int i = 0; i < n; i++)
        {
            lines[i] = s.next();
        }
        int q = s.nextInt();
        String pattern;
        int counter = 0;
        for (int i = 0; i < q; i++)
        {
            pattern = s.next();
            for (int j = 0; j < n; j++)
            {
                if (lines[j].equals(pattern))
                    counter++;
            }
            System.out.println(counter);
            counter = 0;
        }
    }
}
