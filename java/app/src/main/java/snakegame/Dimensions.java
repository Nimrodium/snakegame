
package snakegame;
import snakegame.logic.Shared.Coordinate;

public class Dimensions {
         
    // new , out_of_bounds, to_screen

    public int xmin;
    public int xmax;
    public int ymin;
    public int ymax;
    public Coordinate bounds;
    int scale;
    
    public Dimensions(Coordinate bounds, int scale) {
        int dx = bounds.x()/scale;
        int dy = bounds.y()/scale;

        this.xmin = -dx;
        this.xmax = dx;
        this.ymin = -dy;
        this.ymax = dy;
        this.bounds = bounds;
        this.scale = scale;
    }

    public boolean outOfBounds(Coordinate coords) {
        // return (coords.x() < xmax && coords.x() > xmin && coords.y() < ymax && coords.y() > ymin);
        var x = coords.x();
        var y = coords.y();
        // System.out.println("xmin:" + xmin + "\n xmax:"+ xmax + "\n ymax:"+ ymin + "\n ymax:"+ ymax + "\n bounds:" + bounds);
        return x < this.xmin || x > this.xmax || y < this.ymin || y > this.ymax;
    }

    public Coordinate toScreen(Coordinate coords) {
        int x;
        int y;
        
        if ((coords.x()+bounds.x()/2) < 0) x = 0; else x = (coords.x()+bounds.x()/2);
        if ((bounds.x()/2-coords.y()) < 0) y = 0; else y = (bounds.x()/2-coords.y());

        // var sc = Coordinate.of(coords.x()+bounds.x()/2,coords.y()+bounds.y()/2);

        var sc= Coordinate.of(x, y);
        // System.err.printf("translated %s -> %s\n",coords,sc);
        return sc;
    }

    public Coordinate random() {
        // return Coordinate.of(
        // (int) (Math.random()*((xmax-xmin)/scale + 1)+xmax),
        // (int) (Math.random()*((ymax-ymin)/scale + 1)+ymin)
        // );
        return Coordinate.of(
            (int)(Math.random()*(xmax-xmin)+xmin)+1,
            (int)(Math.random()*(ymax-ymin)+ymin)+1
        );
    }
    public Coordinate getScreenDimensions(){
        return this.bounds;
    }
}