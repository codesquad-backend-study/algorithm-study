package programmers.fia.week10;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Fia메뉴리뉴얼 {
    public List<String> solution(String[] orders, int[] course) {
        Map<String, Integer> allOrder = new HashMap();
        for (String order : orders) {
            String[] split = order.split("");
            boolean[] visited = new boolean[split.length];

            List<String> combination = new ArrayList<>();
            for (int i = 0; i < course.length; i++) {
//                combination.add(combi(split, visited, 0, split.length, i));
            }

            for (int i = 0; i < combination.size(); i++) {
                if (allOrder.containsKey(combination.get(i))) {
                    allOrder.put(combination.get(i), allOrder.get(combination.get(i) + 1));
                    continue;
                }
                allOrder.put(combination.get(i), 1);
            }
        }

        List<String> answer = new ArrayList<>();
        for (String c : allOrder.keySet()) {
            if (allOrder.get(c) > 1) {
                answer.add(c);
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        String[] orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int[] course = {2, 3, 4};

        Fia메뉴리뉴얼 fia메뉴리뉴얼 = new Fia메뉴리뉴얼();
        fia메뉴리뉴얼.solution(orders, course);
    }
}
