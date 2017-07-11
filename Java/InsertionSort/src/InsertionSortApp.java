import javax.swing.*;

public class InsertionSortApp {
    /** main method */
    public static void main(String[] args){
	JFrame mainWindow = new JFrame("Simple Sort App");
	
	// main window settings
	mainWindow.getContentPane().add(new InsertionSortPanel());
	mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	mainWindow.setExtendedState(mainWindow.getExtendedState()|JFrame.MAXIMIZED_BOTH );// wtf is this?
	mainWindow.pack();
	mainWindow.setVisible(true);
    }
}
