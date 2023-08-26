public class Solution {
    // you need to treat n as an unsigned value
    private static int count(int n){
        int cnt = 0;
        while (n > 0) {
            if (n % 2 == 1) {
                cnt++;
            }
            n /= 2;
        }

        return cnt;
    }

    public int hammingWeight(int n) {
        System.out.println(n);

        if (n < 0) {
            return 32 - count(~n);
        }

        return count(n);
    }
}