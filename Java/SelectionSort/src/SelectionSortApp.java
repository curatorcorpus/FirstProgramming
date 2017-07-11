import javax.swing.*;

public class SelectionSortApp {
    public static void main(String[] args){
	// create main window
	JFrame mainWindow = new JFrame("Selection Sort App");
	
	// main window settings
	mainWindow.getContentPane().add(new SelectionSortPanel());
	mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	mainWindow.setExtendedState(mainWindow.getExtendedState()|JFrame.MAXIMIZED_BOTH );
	mainWindow.pack();
	mainWindow.setVisible(true);
    }
}
