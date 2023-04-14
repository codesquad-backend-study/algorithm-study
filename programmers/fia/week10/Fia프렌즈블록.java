package programmers.fia.week10;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Fia프렌즈블록 {

    public int solution(int m, int n, String[] board) {

        List<List<Character>> gameTemp = new ArrayList<>(); // 임시 게임판

        for (String line : board) { // String을 Char로 쪼개서 하나씩 넣는다
            List<Character> temp = new ArrayList<>();
            for (int i = 0; i < line.length(); i++) {
                temp.add(line.charAt(i));
            }
            gameTemp.add(temp);
        }

        List<List<Character>> game = new ArrayList<>(); // 게임판
        for (int j = 0; j < m; j++) {
            List<Character> vertical = new ArrayList<>();
            for (int i = m - 1; i >= 0; i--) { // 리스트의 배치를 변경한다
                vertical.add(gameTemp.get(i).get(j));
            }
            game.add(vertical);
        }

        Set<String> toRemove = new HashSet<>(); // 지워지는 블록의 좌표
        boolean playing = true;
        int count = 0;

        while (playing) {
            // 2개가 붙어있으면 주변을 확인한다
            for (int i = 0; i < n - 1; i++) {
                List<Character> bottom = game.get(i);
                List<Character> up = game.get(i + 1);
                for (int j = 0; j < m - 1; j++) {
                    if (bottom.get(j) == bottom.get(j + 1)) {
                        if (up.size() - 1 > j && up.get(j) == bottom.get(j + 1)) {
                            toRemove.add(i + "," + j);
                            toRemove.add(i + "," + (j + 1));
                            toRemove.add((i + 1) + "," + j);
                            toRemove.add((i + 1) + "," + (j + 1));
                        }
                    }
                }
            }

            count += toRemove.size();
            // 리스트에서 블럭을 제거한다 (뒤에부터 지워야 함)
            for (String remove : toRemove) {
                String[] XY = remove.split(",");
                int x = Integer.parseInt(XY[0]);
                int y = Integer.parseInt(XY[1]);
                game.get(x).remove(y);
            }

            if (toRemove.size() == 0) {
                playing = false;
            }

            toRemove = new HashSet<>();
        }
        return count;
    }
}
