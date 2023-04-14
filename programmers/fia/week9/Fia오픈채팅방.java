package programmers.fia.week9;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Fia오픈채팅방 {
    public List<String> solution(String[] record) {

        Map<String, String> nicknames = new HashMap<>();
        List<String> messages = new ArrayList<>();

        for (String s : record) {
            String[] strings = s.split(" ");
            if (strings[0].equals("Change")) { // 닉네임을 변경하는 경우
                nicknames.put(strings[1], strings[2]);
                continue;
            }
            if (strings[0].equals("Leave")) { // 퇴장하는 경우
                messages.add(strings[0] + " " + strings[1]);
                continue;
            }
            messages.add(strings[0] + " " + strings[1]);
            nicknames.put(strings[1], strings[2]);
        }

        List<String> allMessages = new ArrayList<>();

        for (String m : messages) {
            String[] s = m.split(" ");
            if (s[0].equals("Enter")) {
                allMessages.add(nicknames.get(s[1]) + "님이 들어왔습니다.");
            }
            if (s[0].equals("Leave")) {
                allMessages.add(nicknames.get(s[1]) + "님이 나갔습니다.");
            }
        }

        return allMessages;
    }
}
