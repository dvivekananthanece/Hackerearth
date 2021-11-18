
import java.util.*;
 
class TestClass {
    public static void main(String args[] ) throws Exception {
 
        Scanner s = new Scanner(System.in);
        int N = 0;
        String ans = "No";
        N = s.nextInt();
        
        int[] data = new int[N];
        for(int i=0; i<N; i++){
            data[i] = s.nextInt();
        }
        int res = data[N-1];
        if(res%10 == 0 ){
            ans = "Yes";
        }
        System.out.println(ans);
    }
}