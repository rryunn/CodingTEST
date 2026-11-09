import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {

        HashSet<String> reportSet = new HashSet<>(Arrays.asList(report));
        
        Map<String, Integer> reportedCount = new HashMap<>();
        
        Map<String, HashSet<String>> userReportMap = new HashMap<>();
        
        for(String r: reportSet){
            String[] parts = r.split(" ");
            String reporter = parts[0];
            String target = parts[1];
            
            reportedCount.put(target,reportedCount.getOrDefault(target,0)+1);
            
            userReportMap.putIfAbsent(reporter, new HashSet<>());
            userReportMap.get(reporter).add(target);
        }
        
        HashSet<String> bannedUsers = new HashSet<>();
        for(String user:reportedCount.keySet()){
            if(reportedCount.get(user)>=k){
                bannedUsers.add(user);
            }
        }
        
        int[] answer = new int[id_list.length];
        for(int i=0;i<id_list.length;i++){
            String user = id_list[i];
            
            if(userReportMap.containsKey(user)){
                for(String target: userReportMap.get(user)){
                    if(bannedUsers.contains(target)){
                        answer[i]++;
                    }
                }
            }
        }
        return answer;
        
        
        
        
        
    }
}