package programmers.sully.week5;

import java.util.ArrayList;
import java.util.List;

public class 크레인_인형뽑기_Sully {
    public static int solution(int[][] board, int[] moves) {
        int answer = 0;
        int start = 0;
        List<Integer> basket = new ArrayList<>();

        // 가장 아래 칸부터 쌓이고, 크레인은 가장 위 칸부터 뽑으니까
        for (int i = board.length - 1; i > 0; i--) {
            for (int j = 0; j < board.length; j++) {
                for (int k = start; k < moves.length; k++) {
                    if (moves[k] - 1 == board[i][j]) {
                        basket.add(moves[k] - 1);
                        start++;
                        break;
                    }
                }
            }
        }

        // 연속된 배열 삭제할 떄마다 카운트
        int current = basket.get(0);
        for (Integer b : basket) {
            if (b != current) {
                current = b;
                answer++;
            }
        }

        return answer;
    }
}
