import java.util.*;

class Solution {

    public int solution(int[][] maps) {

        int n = maps.length;
        int m = maps[0].length;

        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];

        // x, y, 거리
        queue.offer(new int[]{0, 0, 1});
        visited[0][0] = true;

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        while (!queue.isEmpty()) {

            int[] cur = queue.poll();

            int x = cur[0];
            int y = cur[1];
            int dist = cur[2];

            // 도착
            if (x == n - 1 && y == m - 1) {
                return dist;
            }

            // 4방향 탐색
            for (int i = 0; i < 4; i++) {

                int nx = x + dx[i];
                int ny = y + dy[i];

                // 범위 확인
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    continue;
                }

                // 벽이거나 방문했으면 패스
                if (maps[nx][ny] == 0 || visited[nx][ny]) {
                    continue;
                }

                visited[nx][ny] = true;
                queue.offer(new int[]{nx, ny, dist + 1});
            }
        }

        return -1;
    }
}