import javax.swing.*;
import java.awt.*;

public class CheckListsApp {
	/** main method */
	public static void main(String args[]){
		// JFrame instantiation
		JFrame frame = new JFrame("Check Lists Application");
		
		// JFrame settings
		frame.setContentPane(new CheckListPanel());
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.pack();
		frame.setVisible(true);
	}
}
