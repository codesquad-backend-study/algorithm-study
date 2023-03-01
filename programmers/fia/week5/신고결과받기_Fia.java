package programmers.fia.week5;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class 신고결과받기_Fia {
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, Integer> count = new HashMap<>();
        for (String id : id_list) {
            count.put(id, 0);
        }

        Map<String, List<String>> users = new HashMap<>();
        for (String id : id_list) {
            users.put(id, new ArrayList<>());
        }

        for (String r : report) {
            String user = r.split(" ")[0];
            String target = r.split(" ")[1];
            if (!users.get(user).contains(target)) {
                count.put(target, count.get(target) + 1);
                users.get(user).add(target);
            }
        }

        List<String> targets = count.entrySet().stream()
                .filter(entry -> entry.getValue() >= k)
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());

        List<Integer[]> results = new ArrayList<>();
        for (int i = 0; i < id_list.length; i++) {
            Integer[] base = {i, 0};
            results.add(base);
        }

        for (String t : targets) {
            for (int i = 0; i < id_list.length; i++) {
                if (users.get(id_list[i]).contains(t)) {
                    results.get(i)[1]++;
                }
            }
        }

        int[] answer = new int[id_list.length];
        for (int i = 0; i < id_list.length; i++) {
            answer[i] = results.get(i)[1];
        }

        return answer;
    }
}
