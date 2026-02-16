package snakegame;

import snakegame.logic.Shared;

public class Main {
    public static void main(String[] args) {
    System.out.println("SNAKEGAME");
    final int SCALE = 20;
    final int FRAME_RATE = 10;
    new Game(FRAME_RATE,SCALE,new Dimensions(Shared.Coordinate.of(500,500),SCALE)).gameLoop();
    }
}
