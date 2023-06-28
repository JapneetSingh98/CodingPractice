class Solution {
    public String gcdOfStrings(String str1, String str2) {

        String min;
        if (str1.length() < str2.length()) {
            min = str1;
        } else {
            min = str2;
        }
        int maxLength = 1;
        for ( int i = min.length(); i > 0; i-- ) {
            if (str1.length() % i == 0 && str2.length() % i == 0) {
                maxLength = i;
                break;
            }
        }

        String curMax = "";
        for ( int i = 0; i < maxLength; i++ ) {
            if (str1.charAt(i) != str2.charAt(i)) {
                return curMax;
            } else {
                double ratio1 = str1.length()/(i+1);
                double ratio2 = str2.length()/(i+1);
                if ((ratio1 % 1 == 0) && (ratio2 % 1 == 0)) {
                    if (str1.equals(str1.substring(0, (i+1)).repeat((int)ratio1)) && str2.equals(str2.substring(0, (i+1)).repeat((int)ratio2))) {
                        curMax = str1.substring(0, (i+1));
                    }
                }

            }
        }
        return curMax;
    }
}