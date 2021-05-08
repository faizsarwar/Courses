public class Account {

    int account_number;
    int balance;
    int annual_interest_rate;
    String date_created;


    public void Deposit(){

    }

    public void WithdrawFunds(){

    }


    public static void main(String[] args){

        System.out.println("Done 11.3");
              
    }

}




public class CheckingAccount extends Account{
    int overdraft_limit;

}




public class SavingAccount extends Account{
    
}
