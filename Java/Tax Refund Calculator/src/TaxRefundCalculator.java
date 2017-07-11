/** Calculates Tax refund (PTS), excludes some conditions
* that are checked 
* TaxRefundCalculator.java
* 
* Basic Algorithm: 
* Actual tax paid  - Theoretical tax paid
*/

import java.util.Scanner;
import java.text.DecimalFormat;

public class TaxRefundCalculator {

	public static void main(String args[]){
		
		// variable declaration
		double income, taxDeducedTheoIncome, totalTaxPaid;
		double taxRefund;
		double totalExternalTax;
		
		final double TAX_RATE1 = 0.105; // income to $14K
		final double TAX_RATE2 = 0.175; // $14K to $48
		final double TAX_RATE3 = 0.3; // $48K to $70
		final double TAX_RATE4 = 0.33; // $70 to over
		
		// object instantiation
		DecimalFormat taxFormat = new DecimalFormat("0.##");
		Scanner input = new Scanner(System.in);
		
		// income main income from job or benefits
		System.out.println("Please Enter Your Total " +
				"Taxable Income Amount (excluding tax): ");
		income = input.nextDouble();
		
		// income from other sources
		// dividends, taxable Maori authority distributions etc
		System.out.println("Please Enter Other Sources Of Taxable" 
							+ " income ie) Bank Interests: ");
		income += input.nextDouble();
		
		// income conditions
		if (income <= 14000)
			taxDeducedTheoIncome = income * TAX_RATE1;
		
		else if (14001 < income && income <= 48000)
			taxDeducedTheoIncome = income * TAX_RATE2;
		
		else if (48000 < income && income <= 70000)
			taxDeducedTheoIncome = income * TAX_RATE3;
		
		else
			taxDeducedTheoIncome = income * TAX_RATE4;
		
		// input total tax paid
		System.out.println("Please Enter Main Total Tax " + 
							"Paid In The Tax Year\n" + 
							"After Less ACC Earners Levy Tax: ");
		totalTaxPaid = input.nextDouble();
		
		// total tax paid from external sources
		System.out.println("Please Enter Total Tax From" 
							+ " Other Sources");
		totalTaxPaid += input.nextDouble();
		
		//tax difference
		taxRefund = (totalTaxPaid - taxDeducedTheoIncome);
		
		//tax refund conditions
		if ((int)taxRefund > 0) 
			System.out.println("IRD owes you approximately: $" + 
						taxFormat.format(taxRefund));
		
		else if ((int)taxRefund == 0)
			System.out.println("That was an accurate tax year!");
		
		else
			System.out.println("You owe IRD approximately: $" + 
						taxFormat.format(taxRefund));
		
		input.close();
	}
}

