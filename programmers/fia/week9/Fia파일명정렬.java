package programmers.fia.week9;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Fia파일명정렬 {
    public List<String> solution(String[] files) {

        // head : 첫 숫자가 등장하기 전까지
        // number : 처음으로 등장한 숫자 : 한 글자에서 최대 다섯 글자까지 가능
        // tail : head와 number를 제외한 나머지 부분

        // Map<String, Integer>에 head와 files의 인덱스를 저장한다.
        // Map<String, Integer>에 numbers와 files의 인덱스를 저장한다.

        // Map의 head를 List에 넣고 정렬한다.
        // 앞과 뒤의 head가 같은 경우 tail을 확인하고 tail도 같은 경우 기존의 순서를 확인하여 정렬한다.

        List<List<Object>> list = new ArrayList<>();

        Pattern head = Pattern.compile("\\D+");
        Pattern number = Pattern.compile("\\d+");

        for (int i = 0; i < files.length; i++) {
            Matcher mHead = head.matcher(files[i]);
            Matcher mNumber = number.matcher(files[i]);

            mHead.find();
            mNumber.find();

            String sHead = mHead.group().toLowerCase();
            String sNumber = mNumber.group();

            list.add(List.of(sHead, Integer.parseInt(sNumber), i));
        }

        Collections.sort(list, (l1, l2) -> {
            String head1 = (String) l1.get(0);
            String head2 = (String) l2.get(0);

            if (head1.equals(head2)) {
                int number1 = (int) l1.get(1);
                int number2 = (int) l2.get(1);
                return Integer.compare(number1, number2);
            }

            return head1.compareTo(head2);
        });

        List<String> answer = new ArrayList<>();

        for (List<Object> l : list) {
            answer.add(files[(int) l.get(2)]);
        }

        return answer;
    }
}
