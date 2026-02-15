package snakegame.renderer;
// import static io.github.libsdl4j.api.Sdl.SDL_Init;
// import static io.github.libsdl4j.api.Sdl.SDL_Quit;

import java.awt.Canvas;
import java.util.Optional;

import javax.swing.JFrame;

import snakegame.Dimensions;
import snakegame.EvaluatedState;
import snakegame.logic.Shared.Direction;
public class Renderer{
    
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
    Dimensions dimensions;
    int scale;
    JFrame window;
    Canvas canvas;
    public Renderer(Dimensions dimensions,int scale){
        this.dimensions = dimensions;
        this.scale = scale;

        this.window = new JFrame("SnakeGame");
        this.window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.window.setSize(dimensions.xmax,dimensions.ymax);
        this.window.setVisible(true);
        /* SDL initialization ... */
    }

    public Optional<GameEvent> getInput(){
        return Optional.empty(); // STUB
    }

    public void drawFrame(EvaluatedState evaluateScene) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    public void update() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    public void clear() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    public void drawDialog(String play) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

}