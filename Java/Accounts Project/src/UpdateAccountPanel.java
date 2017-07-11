import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class UpdateAccountPanel extends JPanel{
	/** instantiate panel */
	private JPanel updateAccountPanel = new JPanel();
	
	/** instantiate components */
	private JLabel accountNumber = new JLabel("Account Number");
	private JLabel accessNumber = new JLabel("Access Number");
	
	
	/** instantiate event listener */
	private EventListener listener = new EventListener();
	
	public UpdateAccountPanel(){
	    // panel settings
	    updateAccountPanel.setPreferredSize(new Dimension(400, 300));
	    
	    // add components
	    updateAccountPanel.add(accountNumber);
	    updateAccountPanel.add(accessNumber);
	    
	    // add listener
	    
	    
	    // add to mainframe
	    add(updateAccountPanel);
	}
	
	private class EventListener implements ActionListener{
	    public void actionPerformed(ActionEvent e){
		
	    }
	}
}
