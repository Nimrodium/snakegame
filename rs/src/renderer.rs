use crate::logic::{CartesianCoordinate, Dimensions, EvaluatedState};

pub enum Event {
    Up,
    Down,
    Left,
    Right,
    Quit,
    PlayPause,
}
/// rendering manager
pub struct Renderer {
    dimensions: Dimensions,
    scale: usize,
    /* ... sdl ... */
}
impl Renderer {
    pub fn draw_frame(&mut self, data: EvaluatedState) {
        todo!()
    }
    pub fn draw_pixel(&mut self, cartesian: CartesianCoordinate) {
        todo!()
    }
    pub fn draw_dialog(&mut self, text: &str) {
        todo!()
    }
    pub fn get_input(&mut self) -> Option<Event> {
        todo!()
    }
}
