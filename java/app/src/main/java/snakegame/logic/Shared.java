package snakegame.logic;

import java.util.function.Function;

public class Shared {
    public static record Coordinate(int x,int y){
        public static Coordinate of(int x,int y){
            return new Coordinate(x,y);
        }
        public Coordinate scale(int scale){
            return Coordinate.of(
                this.x() * scale / 2,
                this.y() * scale / 2
            );
        }
        public Coordinate translate(Function<Integer,Integer> x, Function<Integer,Integer> y){
            return Coordinate.of(x.apply(this.x()),y.apply(this.y()));
        }
        @Override
        public String toString(){
            return String.format("(%d,%d)",x,y);
        }
    }
    public static enum Direction {
        UP,
        DOWN,
        LEFT,
        RIGHT;
    public boolean isOpposite(Direction other) {
        return (this == Direction.UP && other == Direction.DOWN)     ||
               (this == Direction.DOWN && other == Direction.UP)     ||
               (this == Direction.LEFT && other == Direction.RIGHT)  ||
               (this == Direction.RIGHT && other == Direction.LEFT);
        }
    }

    public static boolean isOpposite(Direction d1, Direction d2) {
        return (d1 == Direction.UP && d2 == Direction.DOWN)     ||
               (d1 == Direction.DOWN && d2 == Direction.UP)     ||
               (d1 == Direction.LEFT && d2 == Direction.RIGHT)  ||
               (d1 == Direction.RIGHT && d2 == Direction.LEFT);
    }
}
