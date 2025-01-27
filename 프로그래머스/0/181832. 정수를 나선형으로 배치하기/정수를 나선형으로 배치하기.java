class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int value = 1;
        int col= 0 ;
        int row = 0;
        int direction = 0;
        
        while(value<= n*n){
            answer[row][col] = value;
            value++;
            
            if(direction == 0 ){ //오른쪽으로 쭉~
                if(col == n-1 || answer[row][col+1] != 0){
                    row++;
                    direction = 1;
                }else{
                    col++;
                }
            }
            else if(direction ==1 ){
                if(row == n-1 || answer[row+1][col] != 0){
                    direction = 2;
                    col--;
                }else{
                    row++;
                }
            }
            else if(direction == 2){
                if(col == 0 || answer[row][col-1] != 0){
                    direction = 3;
                    row--;
                }else{
                    col--;
                }
            }
            else if(direction == 3){
                if(row == 0 || answer[row-1][col] != 0){
                    direction = 0;
                    col++;
                    
                }else{
                    row--;
                }
            }
        }

        //오른쪽이 막혀있지 않으면 오른족으로 쭉
        //오른쪽이 막혀있으면or 방문한 곳이면 아래로 가
        //오른쪽과 아래가 막혀있으면 왼쪽으로 가
        //왼쪽과 아래가 막혀있으면 위로 가 
        
        return answer;
    }
}