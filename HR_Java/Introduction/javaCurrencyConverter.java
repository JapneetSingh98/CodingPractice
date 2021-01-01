import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        //System.out.println(payment);
        scanner.close();
        int paymentInt = (int)payment;
        int decimals = (int)((payment - paymentInt) * 100);
        int billions    = paymentInt / 1000000000;
        payment = payment - (billions*1000000000);
        int millions    = (paymentInt % 1000000000) / 1000000;
        payment = payment - (millions*1000000);
        int thousands   = (paymentInt % 1000000) / 1000;
        payment = payment - (thousands*1000);
        int ones    = (paymentInt % 1000);
        
        //System.out.println(billions + " " + millions + " " + thousands + " " + ones + " " + decimals);

        // Write your code here.
        
        String us = "$" + format(billions, millions, thousands, ones, decimals, ",", ".");
        String india = "Rs." + format(billions, millions, thousands, ones, decimals, ",", ".");
        String china = "￥" + format(billions, millions, thousands, ones, decimals, ",", ".");;
        String france = format(billions, millions, thousands, ones, decimals, " ", ",") + " €";
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
        
    }
    
    public static String format(int billions, int millions, int thousands, int ones, int decimals, String spacer, String dec) {
        String num = "";
        boolean zeros = false;
        if (billions != 0) {
            num = num + billions + spacer;
            zeros = true;
        }
        if (millions != 0 || zeros) {
            String mil = Integer.toString(millions);
            if (zeros) {
                while (mil.length() < 3) {
                    mil = "0" + mil;
                }
            }
            num = num + mil + spacer;
        }
        if (thousands != 0 || zeros) {
            String thou = Integer.toString(thousands);
            if (zeros) {
                while (thou.length() < 3) {
                    thou = "0" + thou;
                }
            }
            num = num + thou + spacer;
        }
        if (ones != 0 || zeros) {
            String one = Integer.toString(ones);
            if (zeros) {
                while (one.length() < 3) {
                    one = "0" + one;
                }
            }
            num = num + one + dec;
        }
        String d = Integer.toString(decimals);
        while (d.length() < 2) {
            d = "0" + d;
        }
        num = num + d;
        return num;
    }
}

