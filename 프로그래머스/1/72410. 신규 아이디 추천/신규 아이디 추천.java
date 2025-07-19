class Solution {
    public String solution(String new_id) {
        new_id = new_id.toLowerCase();
        new_id = new_id.replaceAll("[^a-z0-9._-]","");
        //replace는 문자 하나만 처리하는 메서드
        // 정규식을 쓸 때는 반드시 replaceAll
        new_id = new_id.replaceAll("[.]{2,}",".");
        //정규식에서 .은 모든문자이므로 []로 감싸야함. {2,} 이거는 2개이상 연속된것
        new_id = new_id.replaceAll("^\\.|\\.$","");
        // ^ 는 시작 $는 끝. 
        if(new_id.isEmpty()) new_id = "a";

        if(new_id.length()>=16){
            new_id=new_id.substring(0,15);
            if(new_id.charAt(new_id.length()-1)=='.'){
                new_id = new_id.substring(0, new_id.length()-1);
            }
        }
        //split은 문자열로 구분자를 쪼갤 때 쓰는 메서드
        // 문자열을 일부 자를 때에는 substring을 사용하자
        // 자바에서는 문자열에서 []로 문자에 접근 못하고, charAt을 사용해야한다.
        if(new_id.length()<=2){
            while(new_id.length()<3){
                new_id +=new_id.charAt(new_id.length()-1);
            }
        }
        return new_id;
    }
}