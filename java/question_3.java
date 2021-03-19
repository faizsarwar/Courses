public class question_3 {
    
    public static String method2(int a){
       String number = Integer.toHexString(a);
       return number;
    }


    public static void main(String[] args){
       String a = method2(13);
       System.out.println(a);
    }
}
