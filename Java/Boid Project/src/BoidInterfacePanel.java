/**
 * BoidInterfacePanel.java
 * Started: 11th August 2015, Time: 2329
 * @author Jung Woo Park
 * Finished:
 * 
 * main interface panel for flocking simulation
 */

/** import standard java class object libraries */
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;

public class BoidInterfacePanel extends JPanel{
  /** create boid array list */
  private ArrayList <CreateBoid> boids = new ArrayList<CreateBoid>();
  
  /** limit for boid particles */
  private final int LIMIT = 1000;
  
  /** create listener instance */
  private ButtonListener actionListener  = new ButtonListener();
  
  /** creates buttons */
  private JButton startButton = new JButton("Start");
  private JButton stopButton = new JButton("Stop");
  private JButton createBoidButton = new JButton("Create");
  private JButton flock = new JButton("Flock");
  private JButton unflock = new JButton("Unflock");
  
  /** creates labels */
  private JLabel controlLabel = new JLabel("Controls", SwingConstants.CENTER);
  private JLabel createBoids = new JLabel("Create Boids", SwingConstants.CENTER);
  
  /** creates text field */
  private JTextField inputBoidNum = new JTextField();
  
  // delay
  private final int EVENT_DELAY = 0;
  
  // timer to recall events
  private Timer run = new Timer(EVENT_DELAY, actionListener);
  
  /** size of display */
  private final int MONITORWIDTH = 1920, MONITORHEIGHT = 1080;
  
  /** size of control panel */
  private final int PANELWIDTH = 100, PANELHEIGHT = 1080;
  
  /** number of boids to create */
  private int numOfBoids;
  
  /** check whether flock button was pressed */
  private boolean flocking = false;
  
  /** constructor method */
  public BoidInterfacePanel(){
    // create main panel
    JPanel mainPanel = new JPanel();
    
    // main panel settings
    mainPanel.setPreferredSize(new Dimension(1920, 1080));
    mainPanel.setLayout(new GridBagLayout());
    
    // create panel
    JPanel controlPanel = new JPanel();
    
    // grid bag constraints
    GridBagConstraints gbc = new GridBagConstraints();
    gbc.gridx = 0;
    gbc.gridy = 0;
    
    // create gridlayout
    GridLayout grid = new GridLayout(35, 1);
    
    // control Panel settings
    controlPanel.setLayout(grid);
    controlPanel.setPreferredSize(new Dimension(PANELWIDTH, PANELHEIGHT));
    controlPanel.setBackground(new Color(20, 20, 20));
    
    // add listeners 
    flock.addActionListener(actionListener);
    unflock.addActionListener(actionListener);
    startButton.addActionListener(actionListener);
    stopButton.addActionListener(actionListener);
    inputBoidNum.addKeyListener(actionListener);
    createBoidButton.addActionListener(actionListener);
    
    // component settings
    controlLabel.setForeground(Color.white);
    createBoids.setForeground(Color.white);
    
    // add control components
    controlPanel.add(controlLabel);
    controlPanel.add(flock);
    controlPanel.add(unflock);
    controlPanel.add(startButton);
    controlPanel.add(stopButton);
    controlPanel.add(createBoids);
    controlPanel.add(inputBoidNum);
    controlPanel.add(createBoidButton);
    
    // add to main panel
    mainPanel.add(new DrawPanel(), gbc);
    gbc.gridx = MONITORWIDTH - PANELWIDTH;
    mainPanel.add(controlPanel, gbc);
    
    // add to main window
    add(mainPanel);
  }
  
  private class DrawPanel extends JPanel{
    /** drawPanel constructor */
    private DrawPanel(){
      // draw panel settings
      setPreferredSize(new Dimension(MONITORWIDTH - PANELWIDTH, MONITORHEIGHT));
    }
    
    public void paintComponent(Graphics g){
      // refers to inherited constructor
      super.paintComponent(g);
      setBackground(Color.black);
      
      // display boid
      for(int index = 0; index < boids.size(); index++){
        boids.get(index).display(g);
      }
    } // constructor ends 
  }
  
  private class ButtonListener implements KeyListener, ActionListener{
    /** method that creates instances of Boids */
    private void createBoidsInstances(){
      try{
	// empty boid object array list
        boids.clear();

        // gets input from textfield
        numOfBoids = Integer.parseInt(inputBoidNum.getText());
        
        // if number enter exceed set limit
        if(numOfBoids > LIMIT){
          JOptionPane.showMessageDialog(null, "Limit Reached!");
          return;
        }
      } catch(NumberFormatException error){ // catch error if illegal character
        JOptionPane.showMessageDialog(null, "Error Invalid Integer!");
      }
      
      // creates boid particles and captures center point coordinates
      for(int index = 0; index < numOfBoids; index++){
        // create new instance object
        boids.add(index, new CreateBoid());
        
        // if first instance set to alpha
        if(index == 0){
            boids.get(0).setAlpha();
        }
      }
    } // method ends
    
    /** method detects if event has been detected */
    public void actionPerformed(ActionEvent e){
      // if start button is pressed	
      if(e.getSource().equals(startButton)){
        run.start();
      }
      
      // check for possible collision threats
      if(e.getSource().equals(run)){
	  for(CreateBoid boid : boids){
	      boid.collisionDectection(boids, boid);
	  }
        }
      
      // move the object when running
      if(e.getSource().equals(run)){
        for(CreateBoid boid : boids){
          boid.move(flocking, boids);
        }
      }
      
      // if stop button is pressed
      if(e.getSource().equals(stopButton)){
        run.stop();
      }
      
      // if create button is pressed
      else if(e.getSource().equals(createBoidButton)){
        createBoidsInstances();
      }
      
      /** if flock button was pressed execute flocking behaviour */
      else if(e.getSource().equals(flock)){
	  flocking = true;
      }
      
      /** if unflocking button was pressed execute non - flocking behaviour */
      else if(e.getSource().equals(unflock)){
	  flocking = false;
      }
      
      // update instance boids
      repaint();
    }
    
    // if enter is pressed note: working == false
    public void keyPressed(KeyEvent event){
      if(event.getKeyCode() == KeyEvent.VK_ENTER){
      }
    }
    
    // methods that are dormant 
    public void keyTyped(KeyEvent event){}
    public void keyReleased(KeyEvent event){}
  }
}
