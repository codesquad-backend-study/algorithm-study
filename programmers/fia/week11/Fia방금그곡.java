package programmers.fia.week11;

import java.util.ArrayList;
import java.util.List;

public class Fia방금그곡 {
    public String solution(String m, String[] musicinfos) {
        List<Integer> possible = new ArrayList<>();
        String[] titles = new String[musicinfos.length];
        int[] playTimes = new int[musicinfos.length];
        m = m.replace("C#", "c").replace("D#", "d")
                .replace("G#", "g")
                .replace("F#", "f")
                .replace("A#", "a");

        for (int i = 0; i < musicinfos.length; i++) {
            String info = musicinfos[i];
            String[] information = info.split(",");
            String start = information[0];
            String end = information[1];
            String title = information[2];
            String melody = information[3].replace("C#", "c").replace("D#", "d")
                    .replace("G#", "g")
                    .replace("F#", "f")
                    .replace("A#", "a");

            String[] startTime = start.split(":");
            int startHour = Integer.parseInt(startTime[0]);
            int startMin = Integer.parseInt(startTime[1]);

            String[] endTime = end.split(":");
            int endHour = Integer.parseInt(endTime[0]);
            int endMin = Integer.parseInt(endTime[1]);

            int playTime = (endHour * 60 + endMin) - (startHour * 60 + startMin);

            if (melody.length() >= playTime) {
                String playMelody = melody.substring(0, playTime);
                if (playMelody.contains(m)) {
                    possible.add(i);
                    titles[i] = title;
                    playTimes[i] = playTime;
                }
            } else {
                StringBuilder playMelody = new StringBuilder(melody);
                int index = 0;
                while (playMelody.length() != playTime) {
                    playMelody.append(playMelody.charAt(index));
                    index++;
                }
                if (playMelody.toString().contains(m)) {
                    possible.add(i);
                    titles[i] = title;
                    playTimes[i] = playTime;
                }
            }
        }
        if (possible.size() == 0) {
            return "(None)";
        }

        if (possible.size() == 1) {
            return titles[possible.get(0)];
        }

        int titleIndex = -1;
        int maxPlayTime = 0;
        for (int index : possible) {
            if (maxPlayTime < playTimes[index]) {
                titleIndex = index;
                maxPlayTime = playTimes[index]; // 이거 빼먹어서 안된거였음! 정신 나갔네
            }
        }
        return titles[titleIndex];
    }

    public static void main(String[] args) {
        Fia방금그곡 fia방금그곡 = new Fia방금그곡();
        final String solution = fia방금그곡.solution("ABCDEFG", new String[] {"11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"});
        System.out.println("solution = " + solution);
    }
}
