
package fi.tetris;

import fi.tetris.Shape.Tetrominoe;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JButton;
import javax.swing.JPanel;


public class Board extends JPanel {
    
    private final int blockSize = 30;
    private final int boardWidth = 10, boardHeight = 20;
    private int[][] game = new int[boardWidth][boardHeight];    
    private Shape curPiece;
    private Tetrominoe[] tetrominoe;
    private int curX = 0;
    private int curY = 0;
    
    
    public Board() {
 
        JPanel board = new JPanel();
        board.setBounds(0, 0, 400, 600);
        board.setBackground(Color.GRAY);
        
        JButton play = new JButton("play");
        JButton pause = new JButton("pause");
        JButton stop = new JButton("stop");
        
        play.setBounds(50,100,80,30);
        play.setBackground(Color.GREEN);
        board.add(play); 
        board.add(stop);
        board.add(pause);
        add(board);
        //board.paintComponent(g);
        board.setVisible(true);
          
    }
    
    private int squareWidth() {
        return (int) getSize().getWidth() / boardWidth;
    }
    
    private int squareHeight() {
        return (int) getSize().getHeight() / boardHeight;
    }
    
    private Tetrominoe shapeAt(int x, int y) {
        return tetrominoe[(y*boardWidth) + x];
    }
    
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        doDrawing(g);
    }
    
    private void doDrawing(Graphics g) {
        
        var size = getSize();
        int boardTop = (int) size.getHeight() - boardHeight * squareHeight();
        
        for (int i = 0; i < boardHeight; i++) {
            for (int j = 0; j < boardWidth; j++) {
                Tetrominoe shape = shapeAt(j, boardHeight - i - 1);
                if (shape != Tetrominoe.NoShape) {
                    drawSquare(g, j * squareWidth(),
                            boardTop + i * squareHeight(), shape);
                }
            }
        }
        if (curPiece.getShape() != Tetrominoe.NoShape) {
            for (int i = 0; i < 4; i++) {
                int x = curX + curPiece.getX(i);
                int y = curY - curPiece.getY(i);
                drawSquare(g, x*squareWidth(),
                        (boardTop + (boardHeight - y - 1) * squareHeight()),
                        curPiece.getShape());
            }
        }
    }
    
    private void drawSquare(Graphics g, int x, int y, Tetrominoe shape) {

    Color colors[] = {new Color(0, 0, 0), new Color(204, 102, 102),
            new Color(102, 204, 102), new Color(102, 102, 204),
            new Color(204, 204, 102), new Color(204, 102, 204),
            new Color(102, 204, 204), new Color(218, 170, 0)
    };

    var color = colors[shape.ordinal()];

    g.setColor(color);
    g.fillRect(x + 1, y + 1, squareWidth() - 2, squareHeight() - 2);

    g.setColor(color.brighter());
    g.drawLine(x, y + squareHeight() - 1, x, y);
    g.drawLine(x, y, x + squareWidth() - 1, y);

    g.setColor(color.darker());
    g.drawLine(x + 1, y + squareHeight() - 1,
            x + squareWidth() - 1, y + squareHeight() - 1);
    g.drawLine(x + squareWidth() - 1, y + squareHeight() - 1,
            x + squareWidth() - 1, y + 1);
}
    
    /*public static void main(String args[]) {
        new Board();
    }*/
}
