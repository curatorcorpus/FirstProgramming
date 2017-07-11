
public class Accounts {
	/** data fields */
	private int accountNum;
	private String accountName;
	private String accountType;
	private double accountBal;
	private double interestRate;
	private double taxRate;
	private double availableBal;
	
	/** constructor method */
	public Accounts(String accountName,String accountType,int accountNum,double accountBal,
			double interestRate,double taxRate,double availableBal){
		this.accountName = accountName;
		this.accountType = accountType;
		this.accountNum = accountNum;
		this.accountBal = accountBal;
		this.interestRate = interestRate;
		this.taxRate = taxRate;
		this.availableBal = availableBal;
	} // constructor ends

	/** method for change balance */
	public void changeBalance(double accountBal){
		this.accountBal = accountBal;
	} // method ends

	/** returns registered account type */
	public String getAccountType(){
		return accountType;
	} // method ends
	
	/** returns balance of desired account */
	public double getBalance(){
		return accountBal;
	} // method ends
	
	/** returns current interest rate */
	public double getInterestRate(){
		return interestRate;
	} // method ends
	
	/** returns available balance */
	public double getAvailableBal(){
		return availableBal;
	} // method ends
	
	/** returns current tax rate for registra */
	public double getTaxRate(){
		return taxRate;
	} // method ends
}
