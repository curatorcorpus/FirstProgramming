/**
 * BoidsApp.java
 * Started: 11th August 2015, Time: 2329
 * @author Jung Woo Park
 * Finished:
 * 
 * runs the BoidInterfacePanel application
 */

/** import standard java class object libraries */
import javax.swing.*;
import java.awt.*;

public class BoidsApp {
 /** main method */
 public static void main(String args[]){
  // create main window
  JFrame mainWindow = new JFrame("Boid Simulation");
  
  // main window setting
  mainWindow.setExtendedState(JFrame.MAXIMIZED_BOTH);
  mainWindow.getContentPane().add(new BoidInterfacePanel());
  mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  mainWindow.pack();
  mainWindow.setVisible(true);
 }
}
