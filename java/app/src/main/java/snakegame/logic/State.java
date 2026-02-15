package snakegame.logic;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import snakegame.Dimensions;
import snakegame.EvaluatedState;
import snakegame.logic.Shared.Coordinate;
import snakegame.logic.Shared.Direction;
public class State {
    public static enum Scene {
        START,
        PAUSED,
        PLAYING,
        DEAD,
    }
    Snake snake;
    boolean willGrow;
    Optional<Direction> lastDirection;
    Coordinate applePosition;
    Dimensions dimensions;
    Scene scene;
    int score;

    
    public State(Dimensions dimensions){
        this.willGrow = false;    
        this.lastDirection = Optional.empty();
        this.dimensions = dimensions;
        this.applePosition = Coordinate.of(0,0);
        this.snake = new Snake();
        this.score = 0;
        this.scene = Scene.START;
        this.spawnApple();
    }
    
    public void advanceScene(){
        this.scene = switch (this.scene){
            case Scene.START -> Scene.PLAYING;
            case Scene.PAUSED -> Scene.PLAYING;
            case Scene.PLAYING -> Scene.PAUSED;
            case Scene.DEAD -> {
                this.reset();
                yield Scene.PLAYING;
            }
        };
    }
    public int getScore(){
        return this.score;
    }
    public Scene getScene(){
        return this.scene;
    }
    private void reset(){
        this.snake = new Snake();
        this.score = 0x0;
        this.willGrow = false;
        this.spawnApple();
    }

    private void spawnApple(){
        ArrayList<Coordinate> unavailableeCoordinates = (ArrayList<Coordinate>) this.snake.getSegments().clone();
        unavailableeCoordinates.addAll(this.getAdjacentAppleCoordinates());
        
        while (true){
            var randomCoordinate = this.dimensions.random();
            if (!unavailableeCoordinates.contains(randomCoordinate)) 
                break;    
        }
    }

    public EvaluatedState evaluateScene(Optional<Direction> direction) {
        
        Direction filteredDirection;
        if (direction.isPresent()) {
            if (!lastDirection.isEmpty()) {
                if (!Shared.isOpposite(direction.get(), lastDirection.get())) {
                    lastDirection = direction;
                    filteredDirection = direction.get();
                } else {
                    filteredDirection = lastDirection.get();
                }
            } else {
                lastDirection = direction;
                System.out.println("--- Setting last dir. to: " + direction);
                filteredDirection = lastDirection.get();
            }
        } else {
            filteredDirection = lastDirection.get();
        }
        this.moveSnake(Optional.of(filteredDirection));
        willGrow = false;

        if (hasAteApple()) {
            score += 1;
            willGrow = true;
            System.out.println("Apple ate, New Score = " + score);
            spawnApple();
        }
        if (snake.collision(dimensions)) {
            scene = Scene.DEAD;
            System.out.println("You Died! Fucking loserrrrrrrr");
        }
        EvaluatedState evaluated = new EvaluatedState(
            (ArrayList) snake.segments.stream().map(
                seg -> EvaluatedState.Tile.of(seg,EvaluatedState.TileType.SNAKE))
                .toList()
        );
        evaluated.inner.add(EvaluatedState.Tile.of(applePosition,EvaluatedState.TileType.APPLE));
        return evaluated;
        }

    

    private List<Coordinate> getAdjacentAppleCoordinates(){
        
        var range = List.of(-1,0,1);
        var coords = new ArrayList<Coordinate>();
        for (int y: range){
            for (int x: range){
                coords.add(Coordinate.of(x+this.applePosition.x(),y+this.applePosition.y()));
            }
        }
        return coords;
    }

    private void moveSnake(Optional<Direction> direction){
        direction.ifPresent(d -> this.snake.advance(this.willGrow,d));
    }

    private boolean hasAteApple(){
        return this.snake.getHead() == this.applePosition;
    }


    

    
}   
