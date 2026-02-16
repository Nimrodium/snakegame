package snakegame.renderer;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Optional;

import snakegame.logic.Shared.Direction;

public class Input implements KeyListener{
    public enum GameEvent{
        UP, DOWN, LEFT, RIGHT, QUIT, PLAYPAUSE;
        public Optional<Direction> toDirection(){
            return switch (this){
                case UP -> Optional.of(Direction.UP);
                case DOWN -> Optional.of(Direction.DOWN);
                case LEFT -> Optional.of(Direction.LEFT);
                case RIGHT -> Optional.of(Direction.RIGHT);
                default -> Optional.empty();
            };
        }
    }
    private ArrayList<GameEvent> eventQueue;
    public Input(){
        this.eventQueue = new ArrayList();
    }
    public Optional<GameEvent> query(){
        try{
        return Optional.of(this.eventQueue.removeFirst());
        }catch (NoSuchElementException e){
            return Optional.empty();
        }
    }
    @Override
    public void keyTyped(KeyEvent ke) {
        // throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public void keyPressed(KeyEvent ke) {
        // System.err.printf("-- PRESSED -- : [ %s ]\n",ke.getKeyChar());
        // var event = switch (ke){
        //     case ke == KeyEvent.VK_W ||
        // };
        var key = ke.getKeyCode();
        Optional<GameEvent> event;
        event = switch (key) {
            case KeyEvent.VK_W, KeyEvent.VK_UP -> Optional.of(GameEvent.UP);
            case KeyEvent.VK_A, KeyEvent.VK_LEFT -> Optional.of(GameEvent.LEFT);
            case KeyEvent.VK_S, KeyEvent.VK_DOWN -> Optional.of(GameEvent.DOWN);
            case KeyEvent.VK_D, KeyEvent.VK_RIGHT -> Optional.of(GameEvent.RIGHT);
            case KeyEvent.VK_Q -> Optional.of(GameEvent.QUIT);
            case KeyEvent.VK_SPACE -> Optional.of(GameEvent.PLAYPAUSE);
            default -> Optional.empty();
        };
        event.ifPresent(e -> this.eventQueue.add(e));
    }

    @Override
    public void keyReleased(KeyEvent ke) {
        // throw new UnsupportedOperationException("Not supported yet.");
    }
  
}
