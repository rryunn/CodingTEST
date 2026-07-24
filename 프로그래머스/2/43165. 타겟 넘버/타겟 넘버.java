class Solution {
    int result =0;
    int sum =0;
    
    private void bfs(int startNode, int target, int[] numbers, int sum){
        
        if(startNode == numbers.length-1){
            if(sum - numbers[startNode] == target) result = result+1;
            if(sum + numbers[startNode] == target) result = result+1;
        }else {
            bfs(startNode+1,target, numbers,sum+numbers[startNode]);
            bfs(startNode+1, target, numbers, sum-numbers[startNode]);
            }   
        }

    public int solution(int[] numbers, int target) {
        bfs(0, target, numbers, 0);
        return result;
    }
}