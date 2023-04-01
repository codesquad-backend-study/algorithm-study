package programmers.fia.week9;

import java.util.*;

public class Fia주차요금계산 {
    public List<Integer> solution(int[] fees, String[] records) {
        List<Integer> answer = new ArrayList<>();

        // fees : 기본 시간 - 기본 요금 - 단위 시간 - 단위 요금 순으로 들어있다.

        Map<Integer, Integer> in = new HashMap<>(); // 입차 시간
        Map<Integer, Integer> time = new HashMap<>(); // 누적 이용 시간
        Map<Integer, Integer> pay = new HashMap<>(); // 결과적으로 내야하는 요금

        for (String record : records) {
            String[] r = record.split(" ");
            String[] t = r[0].split(":");
            int hour = Integer.parseInt(t[0]) * 60;
            int minute = Integer.parseInt(t[1]);
            int sum = hour + minute;
            int carNumber = Integer.parseInt(r[1]);
            if (r[2].equals("OUT")) { // OUT인 경우 : 사용 시간을 계산하여 누적 이용 시간에 저장한다. 그리고 in에서 제거한다.
                int start = in.get(carNumber);
                if (time.containsKey(carNumber)) { // 이미 누적이 있는 경우 기존의 시간에 더해서 다시 저장한다.
                    time.put(carNumber, time.get(carNumber) + (sum - start));
                } else {
                    time.put(carNumber, sum - start);
                }
                in.remove(carNumber);
             continue;
            }
            // IN인 경우 : Map에 입차 기록을 추가한다.
                in.put(carNumber, sum);
        }

        // 출차 기록이 없는 차량의 이용 시간 계산
        if (in.size() > 0) {
            for (Integer carNumber : in.keySet()) {
                if (time.containsKey(carNumber)) { // 이미 누적이 있는 경우 기존의 시간에 더해서 다시 저장한다.
                    time.put(carNumber, time.get(carNumber) + (1439 - in.get(carNumber)));
                } else {
                    time.put(carNumber, (1439 - in.get(carNumber)));
                }
            }
        }

        // 일괄적으로 요금을 계산한다.
        int basic = fees[0]; // 기본 시간
        int basicPay = fees[1]; // 기본 요금
        int min = fees[2]; // 몇 분마다
        int payMore = fees[3]; // 추가 요금
        for (Integer carNumber : time.keySet()) {
            if (basic >= time.get(carNumber)) { // 기본 요금 안에서 이용한 경우
                pay.put(carNumber, basicPay);
                continue;
            }
            // 기본 요금보다 더 이용한 경우
            int sum = basicPay;
            int useMore = (time.get(carNumber) - basic) / min;
            if ((time.get(carNumber) - basic) % min > 0) {
                sum += payMore;
            }
            pay.put(carNumber, sum + (useMore * payMore));
        }

        List<Integer> sortByCarNumber = new ArrayList<>(pay.keySet()); // 차량 번호는 Map의 Key 값을 넣어서 sort로 정렬한다.
        Collections.sort(sortByCarNumber);
        for (int i = 0; i < sortByCarNumber.size(); i++) { // 차량 번호가 작은 차부터 하나씩 Map에서 찾아와서 List answer에 넣고 반환한다.
            answer.add(pay.get(sortByCarNumber.get(i)));
        }

        return answer;
    }
}
