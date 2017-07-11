import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Arrays;

public class AdminLogin extends JPanel{
	/** instantiation of update panel */
	private JPanel updatePanel = new JPanel();
	
	/** layout instantiation */
	private GridLayout grid = new GridLayout(4,2);
	
	/** instantiate components */
	private JLabel login = new JLabel("Administrator", SwingConstants.RIGHT);
	private JLabel placeholder = new JLabel(" Login");
	private JLabel user = new JLabel("Username:", SwingConstants.CENTER);
	private JLabel pass = new JLabel("Password:", SwingConstants.CENTER);
	private JButton adminLogin = new JButton("Login");
	private JButton reset = new JButton("Reset");
	
	/** instantiate listeners */
	private ButtonListener listener = new ButtonListener();
	
	/** instantiate text fields */
	private TextField username = new TextField();
	private JPasswordField password = new JPasswordField();
	
	/** data field that contains admin name and password */
	private final String ADMIN = "admin";
	private final char[] SETPASSWORD = {'a', 'd', 'm', 'i', 'n'};
	
	private boolean authentication = false;
	
	private JFrame[] checkAuthentication = new JFrame[1];
	
	/** admin login constructor */
	public AdminLogin(JFrame adminLoginWindow){
	    	//admin login window capture
	    	checkAuthentication[0] = adminLoginWindow;
	    
		// JPanel Settings
		updatePanel.setPreferredSize(new Dimension(300,100));
		updatePanel.setLayout(grid);
		
		// component settings
		login.setPreferredSize(new Dimension(300, 50));
		
		// add listeners to components
		username.addKeyListener(listener);
		password.addKeyListener(listener);
		adminLogin.addActionListener(listener);
		reset.addActionListener(listener);
		
		// add components
		updatePanel.add(login);
		updatePanel.add(placeholder);
		updatePanel.add(user);
		updatePanel.add(username);
		updatePanel.add(pass);
		updatePanel.add(password);
		updatePanel.add(adminLogin);
		updatePanel.add(reset);
		
		// add to main frame
		setLocation(600, 500);
		add(updatePanel);
	} // method ends
	
	private class ButtonListener implements KeyListener, ActionListener{
	    	/** method that creates new windows for update selection */
		private void updateSelectionWindow(){
		    // instantiate main window
		    JFrame updateWindow = new JFrame("Account Selector");
			
		    // main window settings
		    updateWindow.getContentPane().add(new UpdateAccountPanel());
		    updateWindow.pack();
		    updateWindow.setVisible(true);
		} // method ends
		
		/** method that check if admin login details are correct */
		public void administrationCheck(){
			// if user and password is right
			if(username.getText().equals(ADMIN) && 
				Arrays.equals(password.getPassword(),SETPASSWORD)){
			    updateSelectionWindow();
			    authentication = true;
			}
			
			if(authentication){
			    checkAuthentication[0].dispose();
			}
			
			// if user and password is right
			else{
			    JOptionPane.showMessageDialog(null, "Incorrect Password! "
						+ "Please Try Again.");
			}
		} // method ends
		
		/** automatically called if event occurs */
		public void actionPerformed(ActionEvent e){
			if(e.getSource().equals(adminLogin)){
			    administrationCheck();
			}
		} // method ends
		
		public void keyPressed(KeyEvent key){
			if(key.getKeyCode() == KeyEvent.VK_ENTER){
			    administrationCheck();
			}
		} // method ends
		
		public void keyTyped(KeyEvent e){} // hibernating method
		public void keyReleased(KeyEvent e){} // hibernating method
	}
}
