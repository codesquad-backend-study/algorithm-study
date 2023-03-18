package programmers.fia.week7;

public class FiaPrimeNumber {
    public int solution(int n, int k) {
        String radix = Integer.toString(n, k);
        String[] split = radix.split("0");

        int count = 0;

        for (String s : split) {
            if (s.equals("") || s.equals("1")) {
                continue;
            }
            if (isPrimeNumber(Integer.parseInt(s))) {
                count++;
            }
        }

        return count;
    }

    public boolean isPrimeNumber(int number) {
        int half = (int) Math.sqrt(number);
        for (int i = 2; i <= half; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        FiaPrimeNumber f = new FiaPrimeNumber();
        System.out.println(f.solution(437674, 3));
        System.out.println(f.solution(110011, 10));
    }
}
