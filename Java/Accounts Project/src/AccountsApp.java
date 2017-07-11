import javax.swing.*;

public class AccountsApp {
	/** main method */
	public static void main(String arg[]){
		// create frame object
		JFrame frame = new JFrame("DNA Bank App Manager");
		
		// Jframe settings
		frame.setLocation(620, 440);
		frame.getContentPane().add(new AccountMainPanel()); // what is this?
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.pack();
		frame.setVisible(true);
	}
}
