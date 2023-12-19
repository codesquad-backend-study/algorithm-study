package programmers.sully.week39;

public class InsertAd {

    public static long toSecond(String time) {
        long second = 0;

        String[] timeSplit = time.split(":");
        int h = Integer.parseInt(timeSplit[0]);
        int m = Integer.parseInt(timeSplit[1]);
        int s = Integer.parseInt(timeSplit[2]);

        second += h < 10 ? Integer.parseInt(timeSplit[0].substring(1)) * 60 * 60 : h * 60 * 60;
        second += m < 10 ? Integer.parseInt(timeSplit[1].substring(1)) * 60 : m * 60;
        second += s < 10 ? Integer.parseInt(timeSplit[2].substring(1)) : s;

        return second;
    }

    public static String toTime(long second) {
        long h = second / 3600;
        long m = (second % 3600) / 60;
        long s = second % 60;

        return toTimeStr(h) + ":" + toTimeStr(m) + ":" + toTimeStr(s);
    }

    public static String toTimeStr(long num) {
        return num < 10 ? "0" + num : String.valueOf(num);
    }

    public static String solution(String playTime, String advTime, String[] logs) {
        long answer = 0;

        long playTimeSecond = toSecond(playTime);
        long advTimeSecond = toSecond(advTime);

        // 초당 시청자 수 (누적합 배열)
        long[] totalViewerForSecond = new long[(int) (playTimeSecond + 1)];

        // 각 구간의 시청자 수 체크
        // totalViewerForSecond[time] = (time 시각에 시작한 시청자 수) - (time 시각에 종료한 시청자 수)
        for (String log : logs) {
            String[] logSplit = log.split("-");
            long startSec = toSecond(logSplit[0]);
            long endSec = toSecond(logSplit[1]);

            totalViewerForSecond[(int) startSec]++;
            totalViewerForSecond[(int) endSec]--;
        }

        // 누적합 계산 1회 (1초 간격으로 누적합 계산)
        // totalViewerForSecond[time] = (time 시각부터 time + 1 시각까지의 1초간의 구간을 포함한 시청자 수)
        for (int i = 1; i < totalViewerForSecond.length; i++) {
            totalViewerForSecond[i] += totalViewerForSecond[i - 1];
        }

        // 누적합 계산 2회 (해당 초까지의 누적 시청자 계산)
        // totalViewerForSecond[time] = (0초부터 time + 1 시각까지의 구간을 포함한 누적 시청자 수)
        for (int i = 1; i < totalViewerForSecond.length; i++) {
            totalViewerForSecond[i] += totalViewerForSecond[i - 1];
        }

        long maxViewerFromZeroTime = totalViewerForSecond[(int) (advTimeSecond - 1)];
        for (int i = 0; i < totalViewerForSecond.length - advTimeSecond; i++) {
            long target = totalViewerForSecond[i + (int) advTimeSecond] - totalViewerForSecond[i];
            if (target > maxViewerFromZeroTime) {
                maxViewerFromZeroTime = target;
                answer = i + 1;
            }
        }

        System.out.println(answer);
        return toTime(answer);
    }

}
