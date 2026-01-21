use crate::logic::{CartesianCoordinate, Dimensions, Direction, EvaluatedState, TileType};
use sdl3;
use sdl3::pixels::Color;

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
// as SDL is a C Native Library it is designed in a rust-unfriendly way,
// where everything holds a reference to everything else, thus to make functions not littered with explicit lifetimes,
// an Rc<Mutex<_>> will be used
pub struct Renderer {
    dimensions: Dimensions,
    scale: usize,
    /* ... sdl ... */
    canvas: Canvas<Window>,
}
impl Renderer {
    // change to thiserror maybe? and have the SDL error be could not initialize SDL, perhaps there is no display server? {e:?}
    pub fn new(dimensions: &Dimensions, scale: usize) -> Result<Self, String> {
        let hint = "perhaps there is no display server running?";
        let sdl_context =
            sdl3::init().map_err(|e| format!("could not initialize SDL3,{hint} : {e:?}"))?;
        let video_subsystem = sdl_context
            .video()
            .map_err(|e| format!("could not initialize video subsystem of SDL3. {hint}: {e:?}"))?;
        let (x, y) = dimensions.get_raster_bounds();
        let window = video_subsystem
            .window("SnakeGame (Rust)", x as u32, y as u32)
            .position_centered()
            .build()
            .map_err(|e| format!("could not initialize SDL3 Window {hint}: {e:?}"))?;

        let mut canvas = window.into_canvas();
        let mut event_pump = sdl_context.event_pump().map_err(|e| format!("{e:?}"));

        Ok(Self {
            dimensions: dimensions.clone(),
            scale,
        })
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

    pub fn update(&mut self) {
        todo!()
    }
}
