package programmers.fia.week6;

import java.util.HashMap;
import java.util.Map;

public class FiaTuple {
    public int[] solution(String s) {
        s = s.replaceAll("\\{|}", "");
        String[] numbers = s.split(",");

        Map<String, Integer> tuple = new HashMap<>();
        for (int i = 0; i < numbers.length; i++) {
            if (tuple.containsKey(numbers[i])) {
                tuple.put(numbers[i], tuple.get(numbers[i]) + 1);
            } else {
                tuple.put(numbers[i], 1);
            }
        }

        int[] number = new int[tuple.size()];
        int[] count = new int[tuple.size()];

        int i = 0;
        for (Map.Entry<String, Integer> entry : tuple.entrySet()) {
            number[i] = Integer.parseInt(entry.getKey());
            count[i] = entry.getValue();
            i++;
        }

        int[] answer = new int[count.length];

        for (int j = 0; j < count.length; j++) {
            int index = count.length - count[j];
            answer[index] = number[j];
        }

        return answer;
    }

    public static void main(String[] args) {
        FiaTuple fiaTuple = new FiaTuple();
        fiaTuple.solution("{{2},{2,1},{2,1,3},{2,1,3,4}}");
    }
}
