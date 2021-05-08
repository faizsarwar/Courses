package employeeearning;
import java.util.*;

public class EmployeeEarning {
 public static void main(String[] args) {
 // TODO code application logic here
 System.out.println("hello world!");
 }

}

class Employee{
 private String name;
// private String[] employee = new String[50];
 private int id;
 double earning = 0;

 Employee(){}

 Employee(String name, int id){
 this.name = name;
 this.id = id;
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