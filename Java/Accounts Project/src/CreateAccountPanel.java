
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CreateAccountPanel extends JPanel{
	/** instantiate JPanel */
	private JPanel accountPanel = new JPanel();
	
	/** instantiate components */
	private JLabel firstname = new JLabel("First Name:", SwingConstants.CENTER);
	private JLabel surname = new JLabel("Surname:", SwingConstants.CENTER);
	private JLabel startingBalance = new JLabel("Starting Balance:", SwingConstants.CENTER);
	private JLabel password = new JLabel("New Password:", SwingConstants.CENTER);
	private JLabel passConfirm = new JLabel("Confirm Password:", SwingConstants.CENTER);
	private JLabel address = new JLabel("Address:", SwingConstants.CENTER);
	private JLabel suburb = new JLabel("Suburb:", SwingConstants.CENTER);
	private JLabel city = new JLabel("City/Town:", SwingConstants.CENTER);
	
	/** define constant value of textfield length */
	private final int LENGTH = 30;
	
	/** panel layout */
	private GridLayout layout = new GridLayout(6, 2);
	
	/** instantiate textfields */
	private TextField accountName = new TextField(LENGTH);
	private JPasswordField accountPass = new JPasswordField(LENGTH);
	private JPasswordField accountConfirmPass = new JPasswordField(LENGTH);
	private TextField accountAddress = new TextField(LENGTH);
	private TextField accountSuburb = new TextField(LENGTH);
	private TextField accountCity = new TextField(LENGTH);
	
	public CreateAccountPanel(){
	    // new window settings
	    accountPanel.setPreferredSize(new Dimension(400,140));
	    accountPanel.setLayout(layout);
		
	    // set component size
		
		
	    // add components
	    accountPanel.add(firstname);
	    accountPanel.add(accountName);
	    accountPanel.add(password);
	    accountPanel.add(accountPass);
	    accountPanel.add(passConfirm);
	    accountPanel.add(accountConfirmPass);
	    accountPanel.add(address);
	    accountPanel.add(accountAddress);
	    accountPanel.add(suburb);
	    accountPanel.add(accountSuburb);
	    accountPanel.add(city);
	    accountPanel.add(accountCity);
		
	    // add to main frame
	    add(accountPanel);
	}
	
}
