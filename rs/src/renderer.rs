use sdl3::pixels::Color;

use crate::logic::{CartesianCoordinate, Dimensions, Direction, EvaluatedState, TileType};

#[derive(Clone, Copy, Debug)]
pub enum Event {
    Up,
    Down,
    Left,
    Right,
    Quit,
    PlayPause,
}
impl Event {
    pub fn to_direction(self) -> Option<Direction> {
        match self {
            Event::Up => Some(Direction::Up),
            Event::Down => Some(Direction::Down),
            Event::Left => Some(Direction::Left),
            Event::Right => Some(Direction::Right),
            Event::Quit => None,
            Event::PlayPause => None,
        }
    }
}
/// rendering manager
pub struct Renderer {
    dimensions: Dimensions,
    scale: usize,
    /* ... sdl ... */
}
impl Renderer {
    pub fn new(dimensions: &Dimensions, scale: usize) -> Self {
        Self {
            dimensions: dimensions.clone(),
            scale,
        }
    }
    pub fn draw_frame(&mut self, data: EvaluatedState) {
        let apple_color = Color {
            r: 255,
            g: 00,
            b: 00,
            a: 255,
        };
        let snake_color = Color {
            r: 00,
            g: 255,
            b: 00,
            a: 255,
        };

        for (cartesian, entity) in data {
            match entity {
                TileType::Snake => self.draw_pixel(cartesian, snake_color),
                TileType::Apple => self.draw_pixel(cartesian, apple_color),
                TileType::Null => (),
            }
        }
    }
    pub fn draw_pixel(&mut self, cartesian: CartesianCoordinate, color: Color) {
        eprintln!("drew pixel at {cartesian:?} with color: {color:?}");
    }
    pub fn draw_dialog(&mut self, text: &str) {
        eprintln!("{}", text)
    }
    pub fn get_input(&mut self) -> Option<Event> {
        None
    }
}
