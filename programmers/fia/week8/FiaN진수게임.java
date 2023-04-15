package programmers.fia.week8;

// 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.
public class FiaN진수게임 {
    public String solution(int n, int t, int m, int p) {
        StringBuilder builder = new StringBuilder();
        int end = t * m; // (게임에 참가하는 인원 * 미리 구해야 하는 수의 개수)가 String의 길이가 된다.

        int number = 0;
        while (builder.length() < end) {
            builder.append(Integer.toString(number, n));
            number++;
        }

        StringBuilder answerBuilder = new StringBuilder();

        for (int i = 0; i < t; i++) {
            answerBuilder.append(builder.charAt(i * m + p - 1));
        }

        return answerBuilder.toString().toUpperCase();
    }
}
