
package snakegame;
import snakegame.logic.Shared.Coordinate;

public class Dimensions {
         
    // new , out_of_bounds, to_screen

    public int xmin;
    public int xmax;
    public int ymin;
    public int ymax;
    // Coordinate abs;
    int scale;

    public Dimensions(Coordinate bounds, int scale) {
        int dx = bounds.x();
        int dy = bounds.y();


        this.xmax = -dx;
        this.xmin = dx;
        this.ymin = -dy;
        this.ymax = dy;
        // abs = bounds;
        this.scale = scale;
    }

    public boolean outOfBounds(Coordinate coords) {
        return (coords.x() < xmax && coords.x() > xmin && coords.y() < ymax && coords.y() > ymin);
    }

    public Coordinate toScreen(Coordinate coords) {
        int x;
        int y;

        if ((coords.x()+xmax) >= 0) x = (coords.x()+xmax); else x = 0; 
        if ((ymax-coords.y()) < 0) y = 0; else y = (ymax-coords.y());
        return Coordinate.of(x, y);
    }

    public Coordinate random() {
        return Coordinate.of(
        (int) (Math.random()*((xmax-xmin)/scale + 1)+xmax),
        (int) (Math.random()*((ymax-ymin)/scale + 1)+ymin));
    }
}