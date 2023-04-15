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

            int playTime = (endHour * 60 - startHour * 60) + (endMin - startMin);

            if (melody.length() >= playTime) {
                String playMelody = melody.substring(0, playTime);
                if (playMelody.contains(m)) {
                    possible.add(i);
                    titles[i] = title;
                    playTimes[i] = playTime;
                }
            } else {
                StringBuilder playMelody = new StringBuilder(melody);
                playMelody.append(melody.charAt(0));
                int index = 1;
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
            }
        }
        return titles[titleIndex];
    }

    public static void main(String[] args) {
        Fia방금그곡 fia방금그곡 = new Fia방금그곡();
        final String solution = fia방금그곡.solution("ABCDEFG", new String[] {"12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"});
        System.out.println("solution = " + solution);
    }
}
