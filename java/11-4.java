import java.util.ArrayList;
import java.util.Collections;
public class Array {
    

public static String  max(ArrayList<Integer> arr){

    if (arr.isEmpty()==true){
        return null;
    }
else{
  int max_value=Collections.max(arr); 
  return String.format("The max value i the list is %d", max_value );
}
}


public static void main(String[] args){
    ArrayList<Integer> numbers = new ArrayList<>();
    numbers.add(0,1);
    numbers.add(1,5);
    numbers.add(2,3);
    String max_value_in_array=max(numbers);
    System.out.println(max_value_in_array);
    
 
}

}
