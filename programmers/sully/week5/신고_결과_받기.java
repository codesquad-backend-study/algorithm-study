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
        System.out.println(reportCntMap);

        // KEY: 유저 ID, VALUE: 유저가 신고한 ID Map 생성 (틀만)
        Map<String, String> reportMap = new HashMap<>();
        int cnt = 0;
        for (int i = 0; i < report.length; i++) {
            String id = report[i].split(" ")[0];
            String report_id = report[i].split(" ")[1];
            // 이미 key 값이 존재하냐 마냐로 처리 (중복 지우기)
            // key 값이 존재하면 value 값이 같은지 다른지 확인 -> 다르면 카운트
            reportMap.put(id, report_id);

            if (!reportMap.get(report[i].split(" ")[0]).equals(report[i].split(" ")[1])) {
                cnt++;
            }
//
            int before = reportCntMap.get(report[i].split(" ")[0]);
            reportCntMap.put(report[i].split(" ")[0], before + cnt);
        }
        System.out.println(reportMap + "\n" + cnt);

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
