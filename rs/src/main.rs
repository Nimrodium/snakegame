// extern crate sdl3;
// use sdl3;
use sdl3;

use crate::{dimensions::Dimensions, game::Game};
mod dimensions;
mod game;
mod logic;
mod renderer;
fn main() {
    let frame_rate = 15;
    let dimensions = Dimensions::new((500, 500));
    let scale = 15;
    Game::new(frame_rate, &dimensions, scale)
        .game_loop()
        .unwrap();
}
