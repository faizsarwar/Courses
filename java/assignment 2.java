import java.util.*;

public class Abc {

    
    List<String> students = new ArrayList<String>();    
    int numberOfStudents = 0;

    public String getName(String p) {
        System.out.println("The cousre is: "+p);
        return p;
    }
    
    public String addStudents(String q){
        numberOfStudents = numberOfStudents + 1;
        students.add(q);
        return q;     
    }

    public void getStudents(){
        System.out.println(students);
    }

    public void getNumberOfStudents(){
        System.out.println("students are: "+numberOfStudents);
    }
        
    public static void main(String[] args){

        Abc a  = new Abc();
        a.getName("DLD");
        a.addStudents("Bosarh pappu");
        a.getStudents();
        a.getNumberOfStudents();
              
    }
}