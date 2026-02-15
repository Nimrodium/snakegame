package snakegame.logic;
import java.util.ArrayList;
import java.util.Arrays;

import snakegame.Dimensions;
import snakegame.logic.Shared.Coordinate;
import snakegame.logic.Shared.Direction;
public class Snake {
    ArrayList<Coordinate> segments;
    public Snake(){
        // this.segments = (ArrayList<Coordinate>) List.of(
         
        // );
        this.segments = new ArrayList<>(Arrays.asList(   
            Coordinate.of(0,0),
            Coordinate.of(2,0),
            Coordinate.of(2,0))
        );
    }
    public ArrayList<Coordinate> getSegments(){
        return this.segments;
    }
    public Coordinate getHead(){
        return this.segments.get(this.segments.size()-1);
    }
    private void addHead(Coordinate head){
        this.segments.add(head);
    }
    private void removeTail(){
        this.segments.remove(0);
    }
    public void advance(boolean willGrow,Direction direction){
        this.moveHead(direction);
        if (!willGrow){
            this.removeTail();
        }
    }
    private void moveHead(Direction direction){
        var head = this.getHead();
        Coordinate newHead = switch (direction){
            case Direction.UP -> new Coordinate(head.x(),head.y()+1);
            case Direction.DOWN -> new Coordinate(head.x(),head.y()-1);
            case Direction.LEFT -> new Coordinate(head.x()-1,head.y());
            case Direction.RIGHT -> new Coordinate(head.x()+1,head.y());
        };
        this.addHead(newHead);
    }
    public boolean collision(Dimensions dimension){
        boolean wallCollision = false;
        if (dimension.outOfBounds(getHead())) {
            wallCollision = true;
        }
        for (Coordinate seg: this.segments) {
            if (seg.equals(getHead())) {
                wallCollision = true;
            }
        }
        return wallCollision;
    }
}
