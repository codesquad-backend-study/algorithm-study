package programmers.fia.week7;

import java.util.*;

public class FiaNews {
    public int solution(String str1, String str2) {
        str1 = str1.toLowerCase().replaceAll("[^a-zA-Z]", ",");
        str2 = str2.toLowerCase().replaceAll("[^a-zA-Z]", ",");

        String[] s1 = str1.split(",");
        String[] s2 = str2.split(",");

        List<String> list1 = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        for (String s : s1) {
            for (int i = 0; i <= s.length() - 2; i++) {
                String two = s.substring(i, i + 2);
                list1.add(two);
            }
        }

        for (String s : s2) {
            for (int i = 0; i <= s.length() - 2; i++) {
                String two = s.substring(i, i + 2);
                list2.add(two);
            }
        }

        if (list1.size() == 0 && list2.size() == 0) {
            return 65536;
        }

        int totalSize= list1.size() + list2.size();

        Set<String> removeDuplicated = new HashSet<>(list1);
        removeDuplicated.addAll(list2);

        int duplicated = totalSize - removeDuplicated.size();

        int answer = duplicated / totalSize;

        if (answer == 1) {
            return 65536;
        }

        double temp = totalSize;
        double result = (duplicated / temp) * 65536;

        return (int) result;
    }

    public static void main(String[] args) {
        FiaNews fiaNews = new FiaNews();
        fiaNews.solution("aa1+aa2", "AAAA12");
    }
}
