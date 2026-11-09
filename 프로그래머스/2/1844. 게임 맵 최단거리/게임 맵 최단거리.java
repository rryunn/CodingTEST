import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        boolean[][] visited= new boolean[n][m];
        
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {0,0,1});
        
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        
        while(!queue.isEmpty()){
            int[] cur = queue.remove();
            int sx= cur[0], sy =cur[1], dist = cur[2];
            visited[sx][sy]=true;
            
            if (sx==n-1 && sy==m-1){
                return dist;
            }
            for (int i=0;i<4;i++){
                int nx = dx[i]+sx;
                int ny = dy[i]+sy;
                
                if (0<=nx && nx<n && ny>=0 && ny<m && !visited[nx][ny]&& maps[nx][ny]==1){
                    visited[nx][ny]=true;
                    queue.add(new int[] {nx,ny,dist+1});
                }
            }
            
        }
        return -1;
    }
}