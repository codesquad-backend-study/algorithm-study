package programmers.fia.week11;

import java.util.Stack;

public class Fia괄호변환 {
    public String solution(String p) {
        StringBuilder builder = new StringBuilder();
        makeCorrect(p, builder);
        return builder.toString();
    }

    public void makeCorrect(String p, StringBuilder builder) {
        if (p.equals("")) {
            return;
        }

        int left = 0;
        int right = 0;
        int index = 0;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                index = i + 1;
                break;
            }
        }

        String u = p.substring(0, index);
        String v = p.substring(index);

        Stack<String> stack = new Stack<>();
        for (int i = 0; i < u.length(); i++) {
            String s = u.substring(i, i + 1);
            if (s.equals("(")) {
                stack.add(s);
            }
            if (s.equals(")") && stack.size() == 0) {
                stack.add(s);
                break;
            }
            if (s.equals(")") && stack.peek().equals("(")) {
                stack.pop();
            }
        }
        if (stack.isEmpty()) {
            builder.append(u);
            makeCorrect(v, builder);
        } else {
            builder.append("(");
            makeCorrect(v, builder);
            builder.append(")");
            String substring = u.substring(1, u.length() - 1);
            for (int i = 0; i < substring.length(); i++) {
                if (substring.charAt(i) == '(') {
                    builder.append(')');
                } else {
                    builder.append('(');
                }
            }
        }
    }

    public static void main(String[] args) {
        Fia괄호변환 fia괄호변환 = new Fia괄호변환();
        final String answer = fia괄호변환.solution("()))((()");
        System.out.println("answer = " + answer);
    }
}
