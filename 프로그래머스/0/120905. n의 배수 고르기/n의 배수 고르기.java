import java.util.*;
//배열은 크기 고정이라서 요소를 제거하려면 list를 써야합니다. 
class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> list = new ArrayList<>();
        
        for(int num : numlist){
            if(num%n==0){
                list.add(num);
            }
        }
        int[] answer = new int[list.size()];
        for(int i=0;i<list.size();i++)
        {
            answer[i] = list.get(i);
        } 
        return answer;
    }
    
}