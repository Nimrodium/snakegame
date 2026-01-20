use std::{thread::sleep, time::Duration};

use crate::{
    logic::{Dimensions, Direction, Scene, State},
    renderer::{Event, Renderer},
};
pub struct Game {
    frame_rate: u64,
    dimensions: Dimensions,
    scale: usize,
}
impl Game {
    pub fn new(frame_rate: u64, dimensions: &Dimensions, scale: usize) -> Self {
        Self {
            frame_rate,
            dimensions: dimensions.clone(),
            scale,
        }
    }
    pub fn step(&self, state: &mut State, renderer: &mut Renderer, direction: Option<Direction>) {
        match state.scene {
            Scene::Start => {
                renderer.draw_dialog("Play!");
            }
            Scene::Paused => {
                renderer.draw_dialog("Unpause");
            }
            Scene::Playing => {
                renderer.draw_frame(state.evaluate(&direction));
            }
            Scene::Dead => {
                renderer.draw_dialog(&format!("You Died!, score {}", state.score));
            }
        }
    }
    pub fn game_loop(&self) {
        let mut state = State::new(&self.dimensions);
        let mut renderer = Renderer::new(&self.dimensions, self.scale);
        let mut i = 0;
        let mut actions = vec![
            Some(Event::PlayPause),
            Some(Event::Up),
            None,
            None,
            None,
            None,
            Some(Event::Left),
            None,
            None,
            Some(Event::Quit),
        ];
        loop {
            println!("Frame {i}; scene={:?}", state.scene);
            // let user_input: Option<Event> = renderer.get_input();
            let user_input = actions[i];
            if let Some(ev) = user_input {
                eprintln!("{ev:?}");
                match ev {
                    Event::Quit => break,
                    Event::PlayPause => state.toggle_playpause(),
                    _ => (),
                }
            }
            sleep(Duration::from_millis(self.frame_rate));
            let direction = user_input.map(|ev| ev.to_direction()).flatten();
            self.step(&mut state, &mut renderer, direction);
            i += 1;
        }
    }
}
