import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        Deque<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        
        queue.offer(new int[] {0,0,1}); //시작점, 거리
        visited[0][0] = true;
        
        int[] dx = {-1,0,1,0};
        int[] dy = {0,1,0,-1};
        
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            int dist = cur[2];
            
            
            if(x==n-1 && y == m-1) return dist;
            for(int i=0;i<4;i++){
                int nx = dx[i] + x;
                int ny = dy[i] + y;
                
                if(nx>=n || nx <0 || ny>=m || ny<0) continue;
                
                if(maps[nx][ny]==0 || visited[nx][ny]) continue;
                
                queue.offer(new int[] {nx,ny, dist+1});
                visited[nx][ny]= true;
            }
        }
        return -1;
    }
}