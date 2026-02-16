package snakegame.renderer;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;

import snakegame.Dimensions;

    class GameWindow extends JFrame implements KeyListener{
        GameFrame frame;
        public GameWindow(GameFrame frame, Dimensions dimensions, Input input){
            super("SnakeGame");
            var bounds = dimensions.getScreenDimensions();
            setSize(new Dimension(bounds.x(),bounds.y()));
            super.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            this.frame = frame;
            super.getContentPane().add(this.frame);
            super.pack();
            super.setLocationRelativeTo(null);
            super.setVisible(true);
            setBackground(Color.BLACK);
            addKeyListener(input);

        }

    @Override
    public void keyTyped(KeyEvent ke) {
        // throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public void keyPressed(KeyEvent ke) {
        System.out.printf("-- PRESSED -- : %s\n",ke);
        // throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public void keyReleased(KeyEvent ke) {
        // throw new UnsupportedOperationException("Not supported yet.");
    }
    }