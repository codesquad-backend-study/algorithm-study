package programmers.sully.week38;

import java.util.*;

class InstallColumnGirder {

    private boolean isValid(Set<List<Integer>> installed) {
        for (List<Integer> each : installed) {
            int x = each.get(0);
            int y = each.get(1);
            int a = each.get(2);

            if (a == 0) {
                if (
                        (y != 0) &&
                                (!installed.contains(Arrays.asList(x, y, 1)) && !installed.contains(Arrays.asList(x - 1, y, 1))
                                        && (!installed.contains(Arrays.asList(x, y - 1, 0)))
                                )
                ) {
                    return false;
                }
            } else if (a == 1) {
                if (
                        (!installed.contains(Arrays.asList(x, y - 1, 0)) && !installed.contains(Arrays.asList(x + 1, y - 1, 0)))
                                && (!installed.contains(Arrays.asList(x - 1, y, 1)) || !installed.contains(
                                Arrays.asList(x + 1, y, 1)))
                ) {
                    return false;
                }
            }

        }

        return true;
    }

    public int[][] solution(int n, int[][] build_frame) {
        Set<List<Integer>> installed = new HashSet<>();

        for (int[] frame : build_frame) {
            int x = frame[0];
            int y = frame[1];
            int a = frame[2];
            int b = frame[3];

            if (b == 0) {
                installed.remove(Arrays.asList(x, y, a));

                if (!isValid(installed)) {
                    installed.add(Arrays.asList(x, y, a));
                }
            } else if (b == 1) {
                installed.add(Arrays.asList(x, y, a));

                if (!isValid(installed)) {
                    installed.remove(Arrays.asList(x, y, a));
                }
            }
        }

        int[][] answer = new int[installed.size()][3];
        int i = 0;
        for (List<Integer> list : installed) {
            answer[i++] = list.stream().mapToInt(Integer::intValue).toArray();
        }

        Arrays.sort(answer, Comparator.comparingInt((int[] a) -> a[0])
                .thenComparingInt(a -> a[1])
                .thenComparingInt(a -> a[2]));

        return answer;
    }

}
