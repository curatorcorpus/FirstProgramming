import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class AccountMainPanel extends JPanel{
	// JPanel instantiation
	private JPanel panel = new JPanel();
	
	// instantiate components
	private JLabel mainMenu = new JLabel("Main Menu of", SwingConstants.RIGHT);
	private JLabel company = new JLabel(" DNA Bank Limited", SwingConstants.LEFT);
	private JButton createAccount = new JButton("Create Account");
	private JButton updateAccount = new JButton("Update Account");
	private ButtonListener eventListener = new ButtonListener();
	
	// main panel settings
	public AccountMainPanel(){
		// panel settings
		panel.setPreferredSize(new Dimension(300, 100));
		panel.setLayout(new GridLayout(2, 2));
		
		// add listeners
		createAccount.addActionListener(eventListener);
		updateAccount.addActionListener(eventListener);
		
		// add components to panel
		panel.add(mainMenu);
		panel.add(company);
		panel.add(createAccount);
		panel.add(updateAccount);
		
		// adds to main panel
		setLocation(600, 500);
		add(panel);
	}
	
	private class ButtonListener implements ActionListener{
		/** calls this window if method called */
		private void createAccount(){
			/** instantiate JFrame */
			JFrame newAccountFrame = new JFrame("Create Account");
			
			// display frame
			newAccountFrame.getContentPane().add(new CreateAccountPanel());
			newAccountFrame.pack();
			newAccountFrame.setLocation(600, 400);
			newAccountFrame.setVisible(true);
		} // method ends
		
		/** calls this window if method called */
		private void updateAccount(){
			/** instantiate JFrame */
			JFrame updateAccountFrame = new JFrame("Administrator Login");
			
			// instantiate JPanel 
			JPanel adminLoginPanel = new AdminLogin(updateAccountFrame);
			
			// display frame
			updateAccountFrame.getContentPane().add(adminLoginPanel);
			updateAccountFrame.pack();
			updateAccountFrame.setLocation(600, 450);
			updateAccountFrame.setVisible(true);
		} // method ends
	
		/** compiler automatically calls this method */
		public void actionPerformed(ActionEvent e){
			
			// if we want to create a new account 
			if(e.getSource().equals(createAccount)){
				createAccount();
			}
			
			// if we want to update an existing account
			if(e.getSource().equals(updateAccount)){
				updateAccount();
			}
		}
	} // listener class ends
} // fin.
