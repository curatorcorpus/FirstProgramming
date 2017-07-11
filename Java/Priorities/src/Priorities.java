import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.awt.event.*;

public class Priorities extends JPanel{
    // instantiate main panel
    private JPanel mainPanel = new JPanel();
    
    // instantiate components for file menu
    private JMenuItem open = new JMenuItem("Open");
    private JMenuItem saveAs = new JMenuItem("Save As");
    private JMenuItem close = new JMenuItem("Close");
    
    // create components
    private JCheckBox comp160 = new JCheckBox("COMP160");
    private JCheckBox bsns106 = new JCheckBox("BSNS106");
    private JCheckBox engl127 = new JCheckBox("ENGL127");
    
    // instantiate components for preferences
    private JMenuItem settings = new JMenuItem("Settings");
    
    private JTextField textField = new JTextField(20);
    
    // checked or unchecked
    private boolean check = false;
    
    public Priorities(JFrame mainWindow){
	// listener instance
	Listener listen = new Listener();
	
	// menu bar components
	JMenuBar menuBar = new JMenuBar();
	JMenu fileMenu = new JMenu("Files");
	JMenu preferencesMenu =  new JMenu("Preferences");
	
	// panel settings
	mainPanel.setPreferredSize(new Dimension(300, 300));
	
	// add menus to mainBar
	menuBar.add(fileMenu);
	menuBar.add(preferencesMenu);
	
	// add menu items to menu
	fileMenu.add(open);
	fileMenu.add(saveAs);
	fileMenu.add(close);
	
	preferencesMenu.add(settings);
	
	// menu settings 
	open.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_O, Event.CTRL_MASK));
	saveAs.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, Event.CTRL_MASK));
	close.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_X, Event.CTRL_MASK));
	
	// add ActionListeners
	open.addActionListener(listen);
	saveAs.addActionListener(listen);
	close.addActionListener(listen);
	
	settings.addActionListener(listen);
	
	// add ItemListeners
	comp160.addItemListener(listen);
	bsns106.addItemListener(listen);
	engl127.addItemListener(listen);
	
	// component settings

	
	// add components
	mainPanel.add(menuBar);
	mainPanel.add(comp160);
	mainPanel.add(bsns106);
	mainPanel.add(engl127);
	
	// set menuBar
	mainWindow.setJMenuBar(menuBar);
	
	// add to main window
	add(mainPanel);
    }
    
    /** listener class */
    private class Listener implements ActionListener, KeyListener, ItemListener{
	// file manipulator
	private JFileChooser fileChooser = new JFileChooser();

	public void actionPerformed(ActionEvent e){
	    // fileChooser return value
	    int returnVal = 0;
	    
	    // captures choosen file
	    File file = null;
	    
	    // buffer reader
	    BufferedReader bReader = null;
	    
	    // current line
	    String currentLine = null;
	    
	    // if open was pressed
	    if(e.getSource().equals(open)){
		returnVal = fileChooser.showOpenDialog(Priorities.this);
		
		if(returnVal == JFileChooser.APPROVE_OPTION){
		    file = fileChooser.getSelectedFile();
		    
		    // read file
		    try{
			bReader = new BufferedReader(new FileReader(file));
			
			// process
			while((currentLine = bReader.readLine()) != null){
			    System.out.println(currentLine);
			}
		    } catch(Exception error){
			error.printStackTrace();
		    }
		}
	    }
	    
	    // if save as was pressed
	    if(e.getSource().equals(saveAs)){
		fileChooser.showSaveDialog(Priorities.this);
	    }
	    
	    // if close was pressed
	    if(e.getSource().equals(close)){
		System.exit(0);
	    }
	    
	    // if settings was pressed
	    if(e.getSource().equals(settings)){
		// instantiate settings window
		JFrame settingWindow = new JFrame("Settings");
		
		settingWindow.getContentPane().add(new Settings());
		settingWindow.pack();
		settingWindow.setVisible(true);
		settingWindow.setLocation(800, 300);
	    }
	}
	
	public void itemStateChanged(ItemEvent e){
	    if(e.getSource() == comp160){
		System.out.println(comp160.isSelected());
	    }
	}
	
	public void keyPressed(KeyEvent e){
	}
	
	// dormant methods
	public void keyTyped(KeyEvent e){}
	public void keyReleased(KeyEvent e){}
    }
}
