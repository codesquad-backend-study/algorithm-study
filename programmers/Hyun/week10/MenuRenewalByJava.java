package programmers.Hyun.week10;

import java.util.*;

public class MenuRenewalByJava {
    public List<String> solution(String[] orders, int[] course) {
        List<String> ans = new ArrayList<>();

        for (int cnt : course) {
            HashMap<String, Integer> courseCandidate = new HashMap<>();

            for (String order : orders) {
                if (order.length() < cnt) continue;

                char[] orderArray = order.toCharArray();
                Arrays.sort(orderArray);
                String sortedOrder = String.valueOf(orderArray);

                List<String> combinations = new ArrayList<>();
                findCombination(0, sortedOrder, "", cnt, combinations);

                for (String combi : combinations) {
                    if (!courseCandidate.containsKey(combi)) {
                        courseCandidate.put(combi, 1);
                    } else {
                        courseCandidate.put(combi, courseCandidate.get(combi) + 1);
                    }
                }
            }

            ArrayList<Map.Entry<String, Integer>> courseEntries = new ArrayList<>(courseCandidate.entrySet());
            courseEntries.sort((Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2) -> {
                return e1.getValue().compareTo(e2.getValue()) * -1;
            });

            if (!courseEntries.isEmpty() && courseEntries.get(0).getValue() >= 2) {
                ans.add(courseEntries.get(0).getKey());

                int next = 1;
                while (courseEntries.size() > next && courseEntries.get(0).getValue() == courseEntries.get(next).getValue()) {
                    ans.add(courseEntries.get(next).getKey());
                    next++;
                }
            }
        }
        Collections.sort(ans);
        return ans;
    }

    private void findCombination(int index, String order, String subCombi, int cnt, List<String> combinations) {
        if (subCombi.length() > cnt) {
            return;
        }

        if (index == order.length()) {
            if (subCombi.length() == cnt) {
                combinations.add(subCombi);
            }
            return;
        }

        findCombination(index + 1, order, subCombi, cnt, combinations);

        subCombi += order.charAt(index);
        findCombination(index + 1, order, subCombi, cnt, combinations);
    }
}
