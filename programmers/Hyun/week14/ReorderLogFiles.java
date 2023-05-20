class Solution {
    public String[] reorderLogFiles(String[] logs) {
        ArrayList<String> digit_logs = new ArrayList<>();
        ArrayList<String[]> letter_logs = new ArrayList<>();

        for (String log : logs) {
            String[] split = log.split(" ", 2);

            if (split[1].matches("[0-9].*")) {
                digit_logs.add(log);
            } else {
                letter_logs.add(split);
            }
        }

        List<String> collect = letter_logs.stream()
                .sorted((log1, log2) -> {
                    if (log1[1].equals(log2[1])) {
                        return log1[0].compareTo(log2[0]);
                    }
                    return log1[1].compareTo(log2[1]);
                })
                .map((log) -> log[0] + " " + log[1])
                .collect(Collectors.toList());

        collect.addAll(digit_logs);

        String[] ans = new String[collect.size()];

        for (int i = 0; i < collect.size(); i++) {
            ans[i] = collect.get(i);
        }

        return ans;
    }
}