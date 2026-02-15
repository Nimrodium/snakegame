package snakegame;

import snakegame.logic.Shared;

public class Main {
    public static void main(String[] args) {
    final int SCALE = 15;
    final int FRAME_RATE = 50;
    new Game(FRAME_RATE,SCALE,new Dimensions(Shared.Coordinate.of(500,500),SCALE)).gameLoop();
    }
}
