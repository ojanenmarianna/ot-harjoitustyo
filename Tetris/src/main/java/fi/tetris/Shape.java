
package fi.tetris;


public class Shape {
    
    protected enum Tetrominoe {
        NoShape, ZShape, SShape, LShape, ReversedLShape, 
        TShape, SquareShape, LineShape
    }
    
    private Tetrominoe piece;
    private int[][] coords;
    
    public Shape() {
        
        coords = new int[4][2];
        setShape(Tetrominoe.NoShape);
    }
    
    public void setShape(Tetrominoe shape) {
        int[][][] coordsTable = new int[][][] {
                {{0, 0}, {0, 0}, {0, 0}, {0, 0}},
                {{0, -1}, {0, 0}, {-1, 0}, {-1, 1}},
                {{0, -1}, {0, 0}, {1, 0}, {1, 1}},
                {{0, -1}, {0, 0}, {0, 1}, {0, 2}},
                {{-1, 0}, {0, 0}, {1, 0}, {0, 1}},
                {{0, 0}, {1, 0}, {0, 1}, {1, 1}},
                {{-1, -1}, {0, -1}, {0, 0}, {0, 1}},
                {{1, -1}, {0, -1}, {0, 0}, {0, 1}}
        };
        
        for (int i = 0; i < 4; i++) {
            System.arraycopy(coordsTable[shape.ordinal()], 0, coords, 0, 4);
        }
        piece = shape;
    }
    
    private void setX(int index, int x) {
        coords[index][0] = x;
    }
    
    private void setY(int index, int y) {
        coords[index][1] = y;
    }
    
    public int getX(int index) {
        return coords[index][0];
    }
    
    public int getY(int index) {
        return coords[index][1];
    }
    
    public Tetrominoe getShape() {
        return piece;
    }
}
