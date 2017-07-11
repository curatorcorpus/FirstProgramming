
import javax.swing.*;

public class AlarmApp {
	/** main method */
	public static void main(String args[]){
	    JFrame mainWindow = new JFrame("Alarm App");
	    
	    // main window settings
	    mainWindow.getContentPane().add(new AlarmPanel());
	    mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    mainWindow.setLocationRelativeTo(null);
	    mainWindow.pack();
	    mainWindow.setVisible(true);
	}
}