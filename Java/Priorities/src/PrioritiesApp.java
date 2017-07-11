import javax.swing.*;
import java.awt.*;

public class PrioritiesApp {
    public static void main(String[] args){
	// create main window
	JFrame mainWindow = new JFrame("Priorities");
	
	// change style
	try { 
	    UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
	} catch (Exception error) {
	    error.printStackTrace();
	}
	
	// main window settings
	mainWindow.getContentPane().add(new Priorities(mainWindow));
	mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	mainWindow.setLocation(800, 300);
	mainWindow.pack();
	mainWindow.setVisible(true);
    }
}
