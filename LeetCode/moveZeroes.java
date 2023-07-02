class Solution {
    public void moveZeroes(int[] nums) {
        int numZeroes = 0;
        for (int i = 0; i < nums.length; i++) {
            if( nums[i] == 0 ) {
                numZeroes++;
            } else {
                if( numZeroes == 0 ) {
                    continue;
                } else {
                    int temp = nums[i];
                    nums[i - numZeroes] = temp;
                    nums[i] = 0;
                }
            }
        }
    }
}