// package employeeearning;
import java.util.*;
import java.util.ArrayList;




public class EmployeeEarning {
 public static void main(String[] args) {
 // TODO code application logic here
 System.out.println("hello world!");

//  System.out.println(numbers);

ArrayList<Employee> numbers = new ArrayList<>();

  hourlyEmp employee1=new hourlyEmp("name1", 1, 24, 2000);
  commissionEmp employee2=new commissionEmp("name2", 2, 3000, 13);
  salaryEmp employee3=new salaryEmp("name3", 2, 2000);

  numbers.add(employee1);
  numbers.add(employee2);
  numbers.add(employee3);

 System.out.println(numbers);


 for (int i=0;i<3;i+=1){
    // System.out.println(numbers.get(i));
    if (numbers.get(i) instanceof commissionEmp==true){
        commissionEmp employe =(commissionEmp) numbers.get(i);
        int current_income=employe.getearning();
        int increament=(int)(current_income*0.1);
        int new_income=(current_income+increament);
        employe.setearning(new_income);
    }
 }

 for (int i=0;i<3;i+=1){
     System.out.println(numbers.get(i).getearning());

 }

}
}


abstract class Employee{
 private String name;
// private String[] employee = new String[50];
 private int id;
 public double earning = 0;

Employee(){};


 Employee(String name, int id){
 this.name = name;
 this.id = id;
 }

 abstract  String getName();

 abstract void setid(int id);

 abstract int getid();

 abstract int getearning();


}



class hourlyEmp extends Employee{
 private String name;
 private int id;
 private int perHour = 10;
 private int total;
 private int earning;

 hourlyEmp(String name, int id, int perHour, int total){
 this.name = name;
 this.id = id;
 this.perHour = perHour;
 this.total = total;
 }
 public String getName() {
 return name;
 }

 public void setid(int id) {
 this.id = id;
 }

 public int getid() {
 return id;
 }
 public int gettotal(){
 return total;
 }
 public int getperHour(){
 return perHour;
 }
 public int getearning(){
 return earning;
 }

 public void setearning(int earning){
    this.earning = earning;
    }

}



class salaryEmp extends Employee{
 private String name;
 private int salary = 200;
 private int earning;
 private int id;



 salaryEmp(String name, int id, int salary){
 this.name = name;
 this.id = id;
 this.salary = salary;
 }
 public String getName() {
 return name;
 }

 public void setid(int id) {
 this.id = id;
 }

 public int getid() {
 return id;
 }
 public int getsalary(){
 return salary;
 }
 public void setearning(int earning){
 this.earning = earning;
 }
 public int getearning(){
 return earning;
 }


}





class commissionEmp extends Employee{
 private String name;
 private double sales = 0.1;
 private int id;
 private int percent;
 private int earning;

 commissionEmp(String name, int id, double sales, int percent){
 this.name = name;
 this.id = id;
 this.sales = sales;
 this.percent = percent;
 }
 
 public String getName() {
 return name;
 }

 public void setid(int id) {
 this.id = id;
 }

 public int getid() {
 return id;
 }
 
 public int percent(){
 return percent;
 }
 public double sales(){
 return sales;
 }
 public void setearning(int earning){
 this.earning = earning;
 }
 public int getearning(){
 return earning;
 }

}