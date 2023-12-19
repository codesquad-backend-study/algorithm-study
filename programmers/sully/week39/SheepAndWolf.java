package programmers.sully.week39;

public class SheepAndWolf {

    private static final int ROOT_INDEX = 0;
    private static final int SHEEP_NUMBER = 0;
    private static final int WOLF_NUMBER = 1;
    private static final int NOT_VISITED_NUMBER = 0;
    private static final int VISITED_NUMBER = 1;

    public int solution(int[] info, int[][] edges) {
        int[] answer = new int[1];
        int[] visited = new int[info.length];

        dfs(1, 0, info, edges, answer, visited);

        return answer[0];
    }

    private void dfs(int sheep, int wolf, int[] info, int[][] edges, int[] answer, int[] visited) {
        if (sheep <= wolf) {
            return;
        }

        answer[0] = Math.max(answer[0], sheep);

        visited[ROOT_INDEX] = VISITED_NUMBER;

        for (int[] edge : edges) {
            int parent_node = edge[0];
            int child_node = edge[1];

            if (visited[parent_node] == VISITED_NUMBER && visited[child_node] == NOT_VISITED_NUMBER) {
                visited[child_node] = VISITED_NUMBER;

                if (info[child_node] == SHEEP_NUMBER) {
                    dfs(sheep + 1, wolf, info, edges, answer, visited);
                } else if (info[child_node] == WOLF_NUMBER) {
                    dfs(sheep, wolf + 1, info, edges, answer, visited);
                }

                visited[child_node] = NOT_VISITED_NUMBER;
            }
        }
    }
}
