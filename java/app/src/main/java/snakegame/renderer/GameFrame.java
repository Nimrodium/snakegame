package snakegame.renderer;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JPanel;

import snakegame.Dimensions;
import snakegame.logic.Shared.Coordinate;

class GameFrame extends JPanel {
        private record Pixel(Rectangle rect,Color color){}

        private final Dimensions dimensions;
        private final int scale;
        private final List<Pixel> pixels = new ArrayList<>();
        
        public GameFrame(Dimensions dimensions, int scale){
            super();
            this.dimensions = dimensions;
            this.scale = scale;
            setBackground(Color.BLACK);
        }
        void drawPixel(Coordinate coordinate,Color color){
            var px = new Pixel(
                new Rectangle(coordinate.x(),coordinate.y(),scale/2,scale/2),
                color
            );
            this.pixels.add(px);
        }
        void clear(){
            this.pixels.clear();
        }
        @Override
        public Dimension getPreferredSize(){
            var bounds = dimensions.getScreenDimensions();
            return new Dimension(bounds.x(),bounds.y());
        }
        @Override
        protected void paintComponent(Graphics g){
            super.paintComponent(g);
            Graphics2D g2 = (Graphics2D) g;
            for (var px:this.pixels){
                g2.setColor(px.color());
                // g2.draw(px.rect());
                g2.fill(px.rect());
            }
        }
    }