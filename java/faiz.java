import java.util.jar.Attributes.Name;

public class customer{
public static String Name;
public static double balance; 

public void RecordPayment(double amountpaid) {
  balance=balance-amountpaid;  
 }


public void RecordCall (int callType, int Min){

    if (callType==1){
        double bill=(0.5*Min);
        balance=balance+bill;
    }

    else if(callType==2) {
        double bill=(2*Min);
        balance=balance+bill;
    }
}

public double displaybalance(){
return balance;
}


public static class goldcustomer extends customer{
    @Override
    public void RecordCall (int callType, int Min){
        if (callType==1){
            double bill=(0.5*Min);
            balance=balance+bill;
        }
        else if(callType==2) {
            if (Min<60){
                double bill=(2*Min);
                balance=balance+bill;
            }
            else if(Min>60)  {
                double bill_1=(2*60);
                double remaining_minutes=(Min-60);
                double bill_2=(0.75*remaining_minutes);
                balance=balance+bill_1+bill_2;
            }
            else{
                System.out.println("NOT RUN");
            }
       
        }
         
    }

}




public static void main(String[] args){

 customer customer1= new customer();
 customer1.balance=50;
 customer1.Name="Faiz";        

customer1.RecordPayment(20);

// System.out.println(customer1.displaybalance());
// customer1.RecordCall(2,15);
// System.out.println(customer1.displaybalance());

// goldcustomer  C2 = new goldcustomer();
// C2.Name="faiz2";
// C2.balance=1.0;
// C2.RecordCall(2,80);
// System.out.println(C2.displaybalance());
}
 

}