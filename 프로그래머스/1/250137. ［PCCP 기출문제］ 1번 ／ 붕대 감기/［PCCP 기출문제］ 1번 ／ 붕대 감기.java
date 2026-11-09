class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {

        int[] real_attack = new int[attacks.length];
        for(int i=0;i<attacks.length;i++){
            real_attack[i] = attacks[i][0];
        }
        
        int lastAttack = attacks[attacks.length-1][0];
        int total=0;
        int t = bandage[0];
        int x = bandage[1];
        int y = bandage[2];
        int real_health = health;
        
        for (int i=0;i<lastAttack+1;i++){
            boolean isAttacked = false;
            
            for(int k=0;k<real_attack.length;k++){
                if (real_attack[k]==i){
                    health -= attacks[k][1];
                    total =0;
                    isAttacked = true;
                    if(health<=0) return -1;
                    break;
                }
            }
            
            
            if(!isAttacked && i>0){
                total+=1;
                health+=x;
                
                if(total==t){
                    health+=y;
                    total=0;
                }
                if(health>=real_health){
                    health = real_health;
                }
            }
        }
        return health;
    }
}