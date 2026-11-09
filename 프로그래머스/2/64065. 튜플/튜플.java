import java.util.*;
class Solution {
    public int[] solution(String s) {
        //문자열-> 배열로 바꾸고
        // , 기준으로 split하고
        //set에다가 있으면 패스 없으면 넣기
        //하고 그걸 배열로 다시 바꿔서 return
        
        s = s.substring(2, s.length()-2);
        String[] arr = s.split("\\}\\,\\{"); 
        
        Arrays.sort(arr, (a,b)->Integer.compare(a.length(), b.length()));
        List<Integer> result= new ArrayList<>();
        Set<String> set = new HashSet<>();
        
        for(String str: arr){
            String[] numbers= str.split(",");
            for(String num : numbers){
                if(!set.contains(num)){
                    set.add(num);
                    result.add(Integer.parseInt(num));
                }
            }
        }
        return result.stream().mapToInt(i->i).toArray();
    }
}