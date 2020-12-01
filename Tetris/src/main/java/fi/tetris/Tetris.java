
package fi.tetris;

import javax.swing.JFrame;
import fi.tetris.Board;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JPanel;

public class Tetris {
    
    public static final int WIDTH = 400, LENGTH = 600;
    private JFrame jframe;
    private Board board;
    private JPanel panelMain;
    
    public Tetris() {
        jframe = new JFrame("Tetris");
        jframe.setSize(WIDTH, LENGTH);
        jframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jframe.setResizable(false);
        jframe.setLocationRelativeTo(null);
        
        panelMain = new JPanel();
        panelMain.setBackground(Color.GRAY);
        panelMain.setBounds(0, 0, 400, 600);
        panelMain.setPreferredSize(new Dimension(200, 400));
        jframe.add(panelMain);
        

        panelMain.add(new Board());
        
        jframe.setVisible(true);
        
    }
    
    
    public static void main(String[] args) {
        new Tetris();
    }
}
