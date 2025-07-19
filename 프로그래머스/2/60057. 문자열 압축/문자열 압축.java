class Solution {
    public int solution(String s) {
        int min = s.length(); // 압축 안 한 길이로 초기화

        for (int len = 1; len <= s.length() / 2; len++) { // 압축 단위 반복
            StringBuilder sb = new StringBuilder(); // 압축된 문자열 저장용
            String prev = s.substring(0, len); // 처음 블록
            int count = 1;

            // len 단위로 잘라가며 비교
            for (int j = len; j <= s.length(); j += len) {
                // 다음 블록 추출: 범위 넘어가면 substring(j)로 처리
                String current = (j + len <= s.length()) 
                    ? s.substring(j, j + len) 
                    : s.substring(j);

                if (current.equals(prev)) {
                    // TODO: 같은 블록이면 count 증가
                    count++;
                } else {
                    // TODO: count가 1보다 크면 sb에 "count + prev" 붙이고
                    if(count>1)sb.append(count).append(prev);
                    else{
                        sb.append(prev);
                    }
                    prev = current;
                    count=1;
                    //       아니면 그냥 prev만 붙이기
                    // 그리고 prev = current, count = 1 초기화
                }
            }

            // TODO: 반복 끝나고 마지막 prev 블록 처리
            // count > 1이면 압축해서 붙이고, 아니면 그냥 붙이기
            if(count>1)
                sb.append(count).append(prev);
            else
                sb.append(prev);
            // TODO: 압축한 길이와 min 중 더 작은 값으로 갱신
            min = Math.min(min, sb.length());
        }

        return min;
    }
}
