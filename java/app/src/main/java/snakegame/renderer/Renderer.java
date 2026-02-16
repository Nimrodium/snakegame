package snakegame.renderer;
// import static io.github.libsdl4j.api.Sdl.SDL_Init;
// import static io.github.libsdl4j.api.Sdl.SDL_Quit;

import java.awt.Color;
import java.util.Optional;

import snakegame.Dimensions;
import snakegame.EvaluatedState;
import snakegame.EvaluatedState.Tile;
import snakegame.EvaluatedState.TileType;
import snakegame.logic.Shared.Coordinate;
import snakegame.renderer.Input.GameEvent;
public class Renderer{
    
  
 
    Dimensions dimensions;
    GameWindow window;
    GameFrame frame;
    Input input;
    int scale;
    
    public Renderer(Dimensions dimensions,int scale){
        this.dimensions = dimensions;
        this.scale = scale;
        this.frame = new GameFrame(dimensions,scale);
        this.input = new Input();
        this.window = new GameWindow(this.frame,dimensions,this.input);
        // this.frame.drawPixel(Coordinate.of(50,5), Color.RED);
    }

    public Optional<GameEvent> getInput(){
        // return Optional.of(GameEvent.UP); // STUB
        return this.input.query();
    }

    public void drawFrame(EvaluatedState evaluatedState) {
        for (Tile px: evaluatedState.inner){
            Color color = switch (px.type()){
                case TileType.SNAKE -> Color.GREEN;
                case TileType.APPLE -> Color.RED;
            };
            this.drawPixel(px.loc(), color);
        }
        // throw new UnsupportedOperationException("Not supported yet.");
    }

    public void update() {
        this.window.repaint();
        // throw new UnsupportedOperationException("Not supported yet.");
    }

    public void clear() {
        this.frame.clear();
        // throw new UnsupportedOperationException("Not supported yet.");
    }

    public void close(){
        this.window.dispose();
        System.exit(0);
    }

    public void drawDialog(String message) {
        System.out.printf("dialog: %s\n",message);
        // throw new UnsupportedOperationException("Not supported yet.");
    }

    // private void pump(){}

    private void drawPixel(Coordinate coordinate,Color color){
        var screenSpace = this.dimensions.toScreen(coordinate.scale(this.scale));
        var sideLength = this.scale/2;
        var corner = screenSpace.translate(x -> x-sideLength,y -> y-sideLength);
        this.frame.drawPixel(corner,color);
        // System.err.printf("drew pixel at %s with color %s\n",coordinate,color);
    }
}
