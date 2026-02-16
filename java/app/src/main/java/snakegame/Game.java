package snakegame;

import java.util.Optional;

import snakegame.logic.Shared;
import snakegame.logic.State;
import snakegame.logic.State.Scene;
import snakegame.renderer.Input.GameEvent;
import snakegame.renderer.Renderer;
class Game {
  int frameRate;
  int scale;
  Dimensions dimensions;

  public Game(int frameRate,int scale,Dimensions dimensions){
    this.frameRate = 1000/frameRate;
    this.dimensions = dimensions;
    this.scale = scale;
  }

  public void step(State state,Renderer renderer,Optional<Shared.Direction> direction){
    
    switch (state.getScene()){
        case Scene.START -> renderer.drawDialog("Play!");
        case Scene.PAUSED -> renderer.drawDialog("Unpause");
        case Scene.PLAYING -> renderer.drawFrame(state.evaluateScene(direction));
        case Scene.DEAD -> renderer.drawDialog("You Died!, score " + state.getScore());
    }
  }
  @SuppressWarnings("BusyWait")
  public void gameLoop(){
    var state = new State(this.dimensions);
    var renderer = new Renderer(this.dimensions,this.scale);
    loop: while (true){
        var input = renderer.getInput();
        if (input.isPresent()){
            switch (input.get()){
                case GameEvent.QUIT -> {renderer.close();}
                case GameEvent.PLAYPAUSE -> state.advanceScene();
            }
        }
        var direction = input.flatMap(event -> event.toDirection());
        renderer.clear();
        this.step(state, renderer, direction);
        renderer.update();
        try{
            Thread.sleep(this.frameRate);
        }catch (InterruptedException e){
            System.err.println("frame sleep interrupted");
        }
        // renderer.clear();
    }
  }
}
