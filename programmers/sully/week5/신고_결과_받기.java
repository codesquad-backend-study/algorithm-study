package programmers.sully.week5;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class 신고_결과_받기 {
    public static int[] solution(String[] id_list, String[] report, int k) {
        int[] countResultMail = {0, 0, 0, 0};

        // KEY: 유저 ID, VALUE: 신고당한 횟수 Map 생성 (틀만)
        Map<String, Integer> reportCntMap = new HashMap<>();
        for (String s : id_list) {
            reportCntMap.put(s, 0);
        }

        // KEY: 유저 ID, VALUE: 유저가 신고한 ID Map 생성 (틀만)
        Map<String, String> reportMap = new HashMap<>();
        for (String s : report) {
            reportMap.put(s, "");
        }

        // report 배열에 따라 신고 횟수 추가 (한 유저가 다른 같은 유저를 계속 신고하면 1번으로 처리)
        int cnt = 0;
        for (int i = 0; i < report.length; i++) {
            String id = report[i].split(" ")[0];
            String report_id = report[i].split(" ")[1];

            // 같은 유저가 다른 같은 유저를 계속 신고하지 않는다는 가정 하에
            if (!reportMap.get(id_list[i]).equals(report_id)) {
                cnt++;
            }
            reportMap.put(id, report_id);

            int before = reportCntMap.get(id_list[i]);
            reportCntMap.put(id_list[i], before + cnt);
        }

        // 2번 이상 신고 당한 유저 추가


        // id_list 순서에 따라 countResultMail(key) 넣고 value 값 대체

        return countResultMail;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(
                solution(
                        new String[]{"muzi", "frodo", "apeach", "neo"},
                        new String[]{"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"},
                        2
                )));
    }
}
