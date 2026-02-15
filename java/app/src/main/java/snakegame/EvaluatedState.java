package snakegame;

import java.util.ArrayList;

import snakegame.logic.Shared.Coordinate;

public class EvaluatedState {
  public enum TileType{
    SNAKE, APPLE
  }
  public record Tile(Coordinate loc,TileType type){
    public static Tile of(Coordinate loc, TileType type){
        return new Tile(loc,type);
    }
  };
    public ArrayList<Tile> inner;
    public EvaluatedState(ArrayList<Tile> inner){
        this.inner = inner;
    }
}
