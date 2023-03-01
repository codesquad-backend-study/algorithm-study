package programmers.Joy.week4;

public class Newid {
    public static void main(String[] args) {
        String result = "";
        String new_id = "abcdefghijklmn.p";

        // 대문자->소문자, 특수문자 제거, 연속된 .제거
        new_id = new_id.toLowerCase();
        new_id = new_id.replaceAll("[~!@#$%^&*()=+\\[{\\]}:?,<>/]","");
        new_id = new_id.replace("."," ");
        new_id = new_id.replaceAll("\\s+",".");
        // 맨앞 맨뒤 . 제거
        if (!new_id.equals("")&&new_id.charAt(0)=='.'){
            new_id = new_id.replaceFirst(".","");
        }
        if (new_id.equals("")){
            new_id = "a";
        }
        if (new_id.charAt(new_id.length()-1)=='.'){
            new_id = new_id.substring(0,new_id.length()-1);
        }
        // 길이에 따라 출력
        if (2<new_id.length()&&new_id.length()<16){
            result = new_id;
        } else if (new_id.length()<3) {
            int n = 3-new_id.length();
            result = new_id+(new_id.charAt(new_id.length()-1)+"").repeat(n);
        }else {
            new_id = new_id.substring(0,15);
            result = (new_id.charAt(14)=='.') ? new_id.substring(0,14): new_id;
        }
        System.out.println(result);
    }
}
