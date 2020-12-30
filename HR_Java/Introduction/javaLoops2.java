import java.util.*;
import java.io.*;
import java.lang.Math;
import java.lang.String;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int cur = a;
            String output = "";
            for(int j = 0; j < n; j++) {
                cur += Math.pow(2, j) * b;
                output = output + " " + cur;
            }
            System.out.println(output.substring(1));
            
        }
        in.close();
    }
}

