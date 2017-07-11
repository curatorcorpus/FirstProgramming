import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CheckListPanel extends JPanel{
	/** data fields */
	private JPanel checkPanel = new JPanel();
	private Checkbox check1 = new Checkbox("First");
	private Checkbox check2 = new Checkbox("Second");
	private Checkbox check3 = new Checkbox("Third");
	
	public CheckListPanel(){
		// JPanel settings
		checkPanel.setPreferredSize(new Dimension(200, 400));
		checkPanel.setBackground(new Color(200, 240, 255));
	
		// add components
		checkPanel.add(check1);
		checkPanel.add(check2);
		checkPanel.add(check3);
		
		// add to main
		add(checkPanel);
	}
	
	private class CheckboxListener implements ItemListener{
		private boolean[] saved = new boolean[3];
		public void itemStateChanged(ItemEvent i){
			if(i.getSource().equals(check1)){
				
			}
		}
	}
}
