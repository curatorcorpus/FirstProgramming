import javax.swing.*; 

public class SliderApp {
    public static void main(String[] args){
	// main window 
	JFrame sliderWindow = new JFrame("Slider Window");
	
	// main window settings 
	sliderWindow.getContentPane().add(new Slider());
	sliderWindow.setLocation(800, 400);
	sliderWindow.setResizable(false);
	sliderWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	sliderWindow.pack();
	sliderWindow.setVisible(true);
    }
}
