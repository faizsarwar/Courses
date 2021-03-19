import java.util.*;  
public class question_three {    
    private static String r;

    public static void main(String args[]){    

    int[] arr = {};       //craeting array to store decimal palindromic primes
    System.out.println(Arrays.toString(arr));
        
    // now checking prime numbers
    int i,m=0,flag=0;      
    for(int n=0;n<=1000;n=n+1){
        m=n/2;     
        if(n==0||n==1){
            // System.out.println(n+" is not prime number");
        }
        else if(n%2==0){    
            // System.out.println(n+" is not prime number");
            }
        else{
            String snum=Integer.toString(n);
            StringBuffer reveresed_number= new StringBuffer(snum);   //creating buffer to reverse it
            reveresed_number.reverse();            // reversing a number
            String reversed=reveresed_number.toString();
            if (Integer.parseInt(reversed)==n){
                //appending array
                arr = Arrays.copyOf(arr, arr.length + 1);
                arr[arr.length - 1] = n; // Assign "n" to the last element
            }
        }
     }//end of else  
    
System.out.println(Arrays.toString(arr));


    }
}    
      