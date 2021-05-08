public class Person{

    String name;
    String phone_number;
    String email;
    String address;


    public String toString(){
        return ("Person name is :    "+ this.name +"Class name is :     "+ this.getClass() );
    }
    
    

    public static void main(String[] args){

        System.out.println("Done 11.1");
              
    }

}




class Student extends Person{


final class status{

    String freshman;
    String junior;
    String senior;
    String sophomor;
}

public String toString(){
    return ("Person name is :    "+ Student.super.name +"Class name is :     "+ Student.class.getName());
}


}




class Employee extends Person {

String office;
String salary;
String date_hired;


public String toString(){
    return ("Person name is :    "+ Employee.super.name +"Class name is :     "+ Employee.class.getName());
}


}




class Faculty extends Employee{

    String office_hours;
    String rank;

    public String toString(){
        return ("Person name is :    "+ Faculty.super.name +"Class name is :     "+ Faculty.class.getName());
    }


}



class Staff extends Employee{

    String tittle;

    public String toString(){
        return ("Person name is :    "+ Staff.super.name +"Class name is :     "+ Staff.class.getName());
    }
}
