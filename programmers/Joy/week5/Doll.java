package programmers.Joy.week5;

public class Doll {
}
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int idx = 0;
        int[] doll = new int[moves.length];

        for (int i : moves){
            for (int j=0;j<board.length;j++){
                if (board[j][i-1]==0) continue;
                doll[idx] = board[j][i-1];
                board[j][i-1] = 0;
                if (idx>0){
                    if (doll[idx]==doll[idx-1]){
                        answer += 2;
                        idx += -2;
                    }
                }
                idx++;
                break;
            }
        }

        return answer;
    }
}
