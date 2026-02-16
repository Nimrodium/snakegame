use std::collections::VecDeque;

use crate::dimensions::{Dimensions, LogicalCoordinate};
use crate::logic::{Direction, EvaluatedState, TileType};
use sdl3::event::Event;
use sdl3::keyboard::Keycode;
use sdl3::pixels::Color;
use sdl3::rect::Rect;
use sdl3::render::Canvas;
use sdl3::video::Window;
use sdl3::{self, EventPump};
#[derive(Clone, Copy, Debug)]
pub enum GameEvent {
    Up,
    Down,
    Left,
    Right,
    Quit,
    PlayPause,
}
impl GameEvent {
    pub fn to_direction(self) -> Option<Direction> {
        match self {
            GameEvent::Up => Some(Direction::Up),
            GameEvent::Down => Some(Direction::Down),
            GameEvent::Left => Some(Direction::Left),
            GameEvent::Right => Some(Direction::Right),
            GameEvent::Quit => None,
            GameEvent::PlayPause => None,
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
    event_queue: VecDeque<Option<GameEvent>>,
    /* ... sdl ... */
    canvas: Canvas<Window>,
    event_pump: EventPump,
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
        let (x, y) = dimensions.get_screen_bounds();
        let window = video_subsystem
            .window("SnakeGame (Rust)", x as u32, y as u32)
            .position_centered()
            .build()
            .map_err(|e| format!("could not initialize SDL3 Window {hint}: {e:?}"))?;

        let canvas = window.into_canvas();
        let event_pump = sdl_context.event_pump().map_err(|e| format!("{e:?}"))?;

        Ok(Self {
            dimensions: dimensions.clone(),
            scale,
            canvas,
            event_pump,
            event_queue: VecDeque::new(),
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
    pub fn draw_pixel(&mut self, cartesian: LogicalCoordinate, color: Color) {
        // let (x, y) = self.scale_coordinate(self.dimensions.to_raster(cartesian));
        let (x, y) = self.dimensions.to_screen(self.scale_coordinate(cartesian));
        let side_length = self.scale / 2;

        let (cx, cy) = (x.saturating_sub(side_length), y.saturating_sub(side_length));
        let rect = Rect::new(cx as i32, cy as i32, side_length as u32, side_length as u32);
        self.canvas.set_draw_color(color);
        self.canvas.fill_rect(rect).unwrap();
        eprintln!(
            "drew pixel at {cartesian:?}:{:?} with color: {color:?}",
            (cx, cy)
        );
    }

    fn scale_coordinate(&self, (x, y): LogicalCoordinate) -> LogicalCoordinate {
        // let scale = |x| x * self.scale / 2;
        // let (dx, dy) = self.dimensions.get_raster_bounds();
        // (scale(x) + (dx / 2), (dy / 2) - scale(y))
        (x * self.scale as isize / 2, y * self.scale as isize / 2)
    }
    pub fn draw_dialog(&mut self, text: &str) {
        eprintln!("{}", text)
    }
    pub fn refresh_input(&mut self) {
        fn match_keycode(k: Keycode) -> Option<GameEvent> {
            match k {
                Keycode::W => Some(GameEvent::Up),
                Keycode::A => Some(GameEvent::Left),
                Keycode::S => Some(GameEvent::Down),
                Keycode::D => Some(GameEvent::Right),

                Keycode::Up => Some(GameEvent::Up),
                Keycode::Left => Some(GameEvent::Left),
                Keycode::Down => Some(GameEvent::Down),
                Keycode::Right => Some(GameEvent::Right),

                Keycode::Space => Some(GameEvent::PlayPause),
                Keycode::Q => Some(GameEvent::Quit),

                _ => None,
            }
        }
        fn map_event(ev: Event) -> Option<GameEvent> {
            match ev {
                Event::Quit { .. } => Some(GameEvent::Quit),
                Event::KeyDown { keycode, .. } => {
                    if let Some(k) = keycode {
                        match_keycode(k)
                    } else {
                        None
                    }
                }
                _ => None,
            }
        }
        self.event_pump.pump_events();
        // let event = self.event_pump.poll_iter();
        // for event in self.event_pump.poll_iter() {}
        let new_events = self
            .event_pump
            .poll_iter()
            .map(|ev| map_event(ev))
            .filter(|ev| ev.is_some());

        self.event_queue.extend(new_events);
    }
    pub fn get_input(&mut self) -> Option<GameEvent> {
        self.refresh_input();
        eprintln!("{:?}", self.event_queue);
        self.event_queue.pop_front().flatten()
    }

    pub fn update(&mut self) {
        self.canvas.present();
    }
    pub fn clear(&mut self) {
        self.canvas.set_draw_color(Color {
            r: 0,
            g: 0,
            b: 0,
            a: 255,
        });
        self.canvas.clear();
    }
}
