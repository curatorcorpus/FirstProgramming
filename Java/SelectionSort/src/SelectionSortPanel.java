import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;

public class SelectionSortPanel extends JPanel{
    // get current monitor size
    private Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
    
    // monitor size
    private final int WIDTH = (int)screenSize.getWidth();
    private final int HEIGHT = (int)screenSize.getHeight();
    private final int CONTROLWIDTH = 120;
    
    // create components
    private JButton sort = new JButton("Sort");
    private JButton stop = new JButton("Stop");
    private JButton restart = new JButton("Restart");
    
    private JLabel controls = new JLabel("Controls", SwingConstants.CENTER);
    
    // create listener
    private Listener listen = new Listener();
    
    // number of rectangles
    private int numOfRectanges = 180;
    
    // array to order 
    private int[] order = new int[numOfRectanges];
    
    // delay
    private int delay = 50;
    
    // run timer
    private Timer run = new Timer(delay, listen);
    
    // current index being used to compare
    private int index = 0;
    private int innerIndexes = 0;
    
    // panel constructor
    public SelectionSortPanel(){
	// random number generator
	Random numGen = new Random();
	
	// create random widths
	for(int index = 0; index < numOfRectanges; index++){
	    int width = numGen.nextInt(1070);
	    order[index] = width;
	}

	JPanel mainPanel = new JPanel();
	JPanel controlPanel = new JPanel();
	
	// main panel settings
	mainPanel.setPreferredSize(new Dimension(WIDTH, HEIGHT));
	mainPanel.setLayout(new GridBagLayout());
	
	// grid bag constraints
	GridBagConstraints gbc = new GridBagConstraints();
	gbc.gridx = 0;
	gbc.gridy = 0;
	
	// create gridlayout
	GridLayout grid = new GridLayout(30, 1);
	
	// control panel settings
	controlPanel.setLayout(grid);
	controlPanel.setBackground(new Color(230, 230, 255));
	controlPanel.setPreferredSize(new Dimension(CONTROLWIDTH, HEIGHT));
	
	// add components
	controlPanel.add(controls);
	controlPanel.add(sort);
	controlPanel.add(stop);
	controlPanel.add(restart);
	
	// add listeners
	sort.addActionListener(listen);
	stop.addActionListener(listen);
	restart.addActionListener(listen);
	
	// add to main panel
	mainPanel.add(new DrawPanel(), gbc);
	gbc.gridx = WIDTH - CONTROLWIDTH;
	mainPanel.add(controlPanel, gbc);
	
	// add to main window
	add(mainPanel);
    }
    
    private class DrawPanel extends JPanel{
	private DrawPanel(){
	    setPreferredSize(new Dimension(1800, 1080));
	}
	
	public void paintComponent(Graphics g){
	    // rectangle width and height local variable
	    final int RECTWIDTH = 9;
	    
	    // call the parent's (JPanel's) constructor
	    super.paintComponent(g);
	    
	    // set background of the draw panel
	    setBackground(Color.black);
		
	    // set rectangle color
	    g.setColor(Color.WHITE);
	    
	    // declare variables for y value and rectangle width index
	    int x = 0;
	    int redrawIndex = 0;
	    
	    // draw all components
	    while(x < (numOfRectanges * 10)){
		// the current index being compared indicated in red
//		if(innerIndexes == index){
//		    g.setColor(Color.red);
//		}
		
		// if the rectangles are sorted
		if(redrawIndex < index){
		    g.setColor(new Color(150, 200, 150));
		    		     //   R    G    B
		}
		
		// indexes that need to be sorted colored in white
		else{
		    g.setColor(Color.WHITE);
		}
		
		g.fillRect(x, (1070-order[redrawIndex]), RECTWIDTH, order[redrawIndex]);
		x += 10;
		redrawIndex++;
	    }
	}
    }
    
    private class Listener implements ActionListener{
	/** selection sorting algorithm */
	private void selectionSort(int outerIndex){
	    for(int innerIndex = outerIndex; innerIndex < order.length; innerIndex++){
		innerIndexes = innerIndex;
		
		// capture current lowest number
		int assumedLowNum = order[outerIndex];
		
		// if there is lower number than the current lowest number, swap
		if(order[innerIndex] < assumedLowNum){
		    swap(outerIndex, innerIndex);
		}
		
		repaint();
	    }
	}
	
	/** method that swap two compared numbers */
	private void swap(int outerIndex, int innerIndex){
	    int currentNum = order[outerIndex];
		
	    // swap
	    order[outerIndex] = order[innerIndex];
	    order[innerIndex] = currentNum;
	}
	
	// if button event is detected
	public void actionPerformed(ActionEvent e){
	    // if start/sort button was pressed
	    if(e.getSource() == sort){
		run.start();
	    }
	    
	    // if timer is running / artificial loop created by events from timer
	    if(e.getSource() == run){
		// if index is under array size
		if(index < order.length){
		    selectionSort(index);
		    index++;
		}
		
		// if index is over array size
		else{
		    run.stop();
		}
		repaint();
	    }
	    
	    // if stop button was pressed
	    if(e.getSource() == stop){
		run.stop();
	    }
	    
	    // if restart button was pressed
	    if(e.getSource() == restart){
		// random number generator
		Random numGen = new Random();
		
		// restart the index
		index = 0;
		
		// create random widths
		for(int index = 0; index < numOfRectanges; index++){
		    int width = numGen.nextInt(1070);
		    order[index] = width;
		}
		
		repaint();
	    }
	}
    }
}
