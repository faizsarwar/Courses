import java.util.*;  
class UserInputDemo   
{  
public static void main(String[] args)  

{  
Scanner sc= new Scanner(System.in);    //System.in is a standard input stream  
System.out.print("Enter length of array- ");  
int a= sc.nextInt();  
int z =a;
      // with no element
int s=0;
int[] matrix[]=new int[a][a];
for(int i=0;i!=a;i=i+1){
    int lsit[]=new int[a];
    for(;a!=0;a=a-1){
        System.out.print("Enter first number- ");  
        int b= sc.nextInt();
        lsit[s]=b;
        s=s+1;
    }
    a=z;
    s=0;
    matrix[i]=lsit;
}

System.out.println("Your Array is :     ");


for (int[] element: matrix) {
    System.out.println(Arrays.toString(element));
};

for (int i=0;i!=a;i=i+1){
    matrix[i][i]=1;
}

System.out.println("The new matrix with diagonal of value 1 is :     ");

for (int[] element: matrix) {
    System.out.println(Arrays.toString(element));
};

}  
}  