package programmers.sully.week2;

import java.util.Arrays;

public class SecretMapSully {
    // 암호 해독
    // 각 칸은 "", "#" 두 종류
    // 지도1 + 지도2 -> 2진수로 암호화 됨
    // 벽: "#", 공백: ""
    public String[] solution(int n, int[] arr1, int[] arr2) {
        // 풀이 순서
        // 10진수 -> 2진수 (바이너리 스트링)
        // 1이면 "#", 0이면 ""으로 변환
        // 지도1, 지도2 비교하면서 합치고 answer 배열에 담기
        String[] answer = {};

        String[] arr1ToBinaryString = new String[n];
        String[] arr2ToBinaryString = new String[n];

        // 10진수 int[] -> 2진수 String[]
        for (int i = 0; i < n; i++) {
            String[] tmpArr1 = new String[n];
            String[] tmpArr2 = new String[n];

            // 문제점 1: 이진수로 변환하는 과정에서 첫번째 숫자가 0인 경우, 0을 빼고 저장함
            // 해결 방안: 5글자가 아닌 경우 -> if 문으로 0을 집어넣어 주기

            // arr1: 이진수로 변환 String 배열
            tmpArr1[i] = Integer.toBinaryString(arr1[i]);
            System.out.println((i + "번째 tmpArr1: " + Arrays.toString(tmpArr1)));

            // arr2: 이진수로 변환 String 배열
            tmpArr2[i] = Integer.toBinaryString(arr2[i]);
            System.out.println((i + "번째 tmpArr2: " + Arrays.toString(tmpArr1)));


            // 문제점 2: binaryString 형태를 각각 0이냐 1이냐에 따라 공백, #으로 바꿔줘야 하는데 로직 잘못 짬
            // 해결 방안: for문과 StringBuilder를 써서 append 후 저장하는 건 어떨까?

            // tmpArr1 배열에 이진수가 저장돼 있으니 -> 이진수를 공백과 #으로 바꾸는 과정
            // tmpArr1[i]의 length가 4이하인 경우 앞자리에 공백 넣어주기
            for (int j = 0; j < tmpArr1.length; j++) {
                if (tmpArr1.length < 5) { // 앞자리 공백 넣어주기

                }
            }
            System.out.println((i + "번째 arr1ToBinaryString: " + Arrays.toString(arr1ToBinaryString)));

            // tmpArr2 배열에 이진수가 저장돼 있으니 -> 이진수를 공백과 #으로 바꾸는 과정
            System.out.println((i + "번째 arr2ToBinaryString: " + Arrays.toString(arr2ToBinaryString)));
        }

        System.out.println("최종 arr1ToBinaryString: " + Arrays.toString(arr1ToBinaryString));
        System.out.println("최종 arr2ToBinaryString: " + Arrays.toString(arr2ToBinaryString));

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new SecretMapSully().solution(5, new int[]{9, 20, 28, 18, 11}, new int[]{30, 1, 21, 17, 28})));
    }
}
