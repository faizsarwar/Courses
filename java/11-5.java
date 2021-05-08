import java.util.ArrayList;

public class Course {
    
    private String courseName;
    
    private ArrayList<String> students = new ArrayList<String>();
    
    private int numberOfStudents;
    
    public Course(String courseName) {
    this.courseName = courseName;
    }

    public void addStudent(String student) {
    students.add(student);
    numberOfStudents++;
    }
    
    public ArrayList<String> getStudents() {
    return students;
    } 
    
    public int getNumberOfStudents() {
    return numberOfStudents;
    } 

    public String getCourseName() {
    return courseName;
    }

    public void dropStudent(String student) {
    // Left as an exercise in Programming Exercise 10.9
    }
    

    public static void main(String[] args){

        System.out.println("Added Array list replacing array to store students");
              
    }

}