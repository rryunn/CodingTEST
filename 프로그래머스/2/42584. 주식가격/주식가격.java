class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        
        for(int i=0; i<prices.length; i++){
            int check = prices[i];
            int count =0;
                for(int j=i+1;j<prices.length;j++){
                    if(prices[i]>prices[j]){
                        count+=1;
                        break;
                    }else{
                        count+=1;
                    }
                }
            answer[i] = count;
        }
        return answer;
    }
}