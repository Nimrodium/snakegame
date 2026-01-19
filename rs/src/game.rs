use crate::logic::Dimensions;
struct State {}

pub struct Game {
    frame_rate: isize,
    dimensions: Dimensions,
}
impl Game {
    pub fn new() -> Self {
        Self {}
    }
    pub fn step(&self, state: &mut State) {}
    pub fn game_loop(&self) {}
}
