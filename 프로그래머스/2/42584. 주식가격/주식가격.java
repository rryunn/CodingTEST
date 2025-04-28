class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] res = new int[n];
      
            
        for(int i =0; i<n; i++){
            int count =0;
            for (int j = i+1; j<n; j++){
                if(prices[i] <= prices[j])
                    count++;
                else {count++; break;}
                   
            }
            res[i] = count;
            
        }
        return res;
    }
}