import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JFrame;
import javax.swing.JPanel;

/**
 * An applet that displays the standard fonts and styles available in Java 1.1
 */
public class FontFam extends JPanel {
  // The available font families
  String[] families = { "Serif", // "TimesRoman" in Java 1.0
      "SansSerif", // "Helvetica" in Java 1.0
      "Monospaced" }; // "Courier" in Java 1.0

  // The available font styles and names for each one
  int[] styles = { Font.PLAIN, Font.ITALIC, Font.BOLD,
      Font.ITALIC + Font.BOLD };

  String[] stylenames = { "Plain", "Italic", "Bold", "Bold Italic" };

  // Draw the applet.
  public void paint(Graphics g) {
    for (int f = 0; f < families.length; f++) { // for each family
      for (int s = 0; s < styles.length; s++) { // for each style
        Font font = new Font(families[f], styles[s], 18); // create font
        g.setFont(font); // set font
        String name = families[f] + " " + stylenames[s]; // create name
        g.drawString(name, 20, (f * 4 + s + 1) * 20); // display name
      }
    }
  }

  public static void main(String[] a) {
    JFrame f = new JFrame();
    f.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    f.setContentPane(new FontFam());
    f.setSize(300,300);
    f.setVisible(true);
  }

}


