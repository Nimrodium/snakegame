// extern crate sdl3;
// use sdl3;
use sdl3;

use crate::{game::Game, logic::Dimensions};
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
