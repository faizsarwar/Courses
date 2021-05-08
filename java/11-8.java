import java.sql.Date;
import java.util.ArrayList;


public class Account{
    private int id=0;
    private double balance=0;
    private double annualinterestrate=0;
    private Date dateCreated;
    public String name;
    public ArrayList<Transaction> transactions;

    public Account(){
    
    }

    public Account(String name,int id,double balance){
        this.name=name;
        this.id=id;
        this.balance=balance;

    }

    public  double GetMonthlyinterestrate(double rate){
        return (annualinterestrate/12)*rate;
    }

    public void deposit(double amount){
        
        balance=balance+amount;

        Transactions action=new Transaction();
        action.type="deposit";
        action.amount=amount;
        action.balance=balance;
        action.description="dopisted sucessfully";
        transactions.add(action);

        

    }



    public void withdraw(double amount){
        balance=balance-amount;
    
        Transactions action=new Transaction();
        action.type="withdraw";
        action.amount=amount;
        action.balance=balance;
        action.description="withdraw sucessfully";
        transactions.add(action);

    
    }


    public double GetMonthlyinterest(){
        return (annualinterestrate/12);
    }



    public static void main(String[] args){
        Account a1=new Account();
        a1.deposit(100);
        System.out.println(a1.balance);
              
    }


}

public class Transaction{
    String type;
    double amount;
    double balance;
    String description; 
}
