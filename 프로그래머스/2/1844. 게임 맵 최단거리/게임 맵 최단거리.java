import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        Deque<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        
        queue.offer(new int[] {0,0,1});
        visited[0][0] = true;
        
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            int dist = cur[2];
            
            
            int[] dx = {-1,0,1,0};
            int[] dy = {0,1,0,-1};
            
            for(int i =0;i<4;i++){
                int nx = dx[i] + x;
                int ny = dy[i] + y;
                
                if(nx == n-1 && ny == m-1) return dist+1;
                
                if(nx<0 || ny <0 || nx>=n || ny>=m || maps[nx][ny]==0) continue;
                
                if(visited[nx][ny]) continue;
                
                queue.offer(new int[] {nx,ny,dist+1});
                visited[nx][ny] = true;
                
            }
        }
        return -1;
    }
}