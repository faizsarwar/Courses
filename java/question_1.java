import java.util.Random; 
import java.util.*;
// import org.apache.commons.lang.ArrayUtils;
public class question_1 {


  public static void main(String[] args) {

    Random r = new Random();
    char[] real = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

    char[] array = new char[100];

    for(int i = 0; i < array.length; i++){

      array[i] = (char)(r.nextInt(26) +97);

      }
      System.out.println(Arrays.toString(array));
        
    
    String[] counter=new String[26];
    for(int j=0; j< real.length; j++){
        int count=0;
        for(int i=0; i< array.length; i++){

            if (real[j]==array[i]){
                count=count+1;
            }
        }
        counter[j] = String.format("character %s is occured %x times",real[j],count+1);          
    }


  System.out.println(Arrays.toString(counter));


}
}
