package src.logic;

import java.util.List;
public class Snake {
    ArrayList<Coordinate> segments;
    public Snake(){
        this.segments = List.of(
            new Coordinate(0,0),
            new Coordinate(2,0),
            new Coordinate(2,0)
        );
    }
    private Coordinate getHead(){
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
            self.removeTail();
        }
    }
    private void moveHead(Direction direction){
        var head = this.getHead();
        Coordinate newHead = switch direction{
            case Direction.UP -> new Coordinate(head.x,head.y+1);
            case Direction.DOWN -> new Coordinate(head.x,head.y-1);
            case Direction.LEFT -> new Coordinate(head.x-1,head.y);
            case Direction.RIGHT -> new Coordinate(head.x+1,head.y);
        }
        this.addHead(head);
    }
    public boolean collision(Dimension dimension){
    }
}
