package snakegame.logic;
public class Shared {
    public static record Coordinate(int x,int y){
        public static Coordinate of(int x,int y){
            return new Coordinate(x,y);
        }
    }
    public static enum Direction {
        UP,
        DOWN,
        LEFT,
        RIGHT,
    }

    public static boolean isOpposite(Direction d1, Direction d2) {
        return (d1 == Direction.UP && d2 == Direction.DOWN)     ||
               (d1 == Direction.DOWN && d2 == Direction.UP)     ||
               (d1 == Direction.LEFT && d2 == Direction.RIGHT)  ||
               (d1 == Direction.RIGHT && d2 == Direction.LEFT);
    }
}
