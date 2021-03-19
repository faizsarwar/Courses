import java.util.Arrays;
import java.util.*;
public class question_2 {


    static void myMethod(int a) {

        System.out.println("The factors are: ");
        List<Integer> values = new ArrayList<Integer>();
        int counter=0;
        for(int i = 1 ; i <= a;i++){
            if(a%i==0){
                values.add(i);
                counter=counter+1;
            }
        }
        System.out.println(values); 
    }      
   
    public static void main(String[] args) {
        myMethod(8);
    }
    
}