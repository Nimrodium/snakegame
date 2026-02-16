use std::{thread::sleep, time::Duration};

use crate::{
    dimensions::Dimensions,
    logic::{Direction, Scene, State},
    renderer::{GameEvent, Renderer},
};
pub struct Game {
    frame_rate: u64,
    dimensions: Dimensions,
    scale: usize,
}
impl Game {
    pub fn new(frame_rate: u64, dimensions: &Dimensions, scale: usize) -> Self {
        Self {
            frame_rate:1000/frame_rate,
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
    pub fn game_loop(&self) -> Result<(), String> {
        let mut state = State::new(&self.dimensions);
        let mut renderer = Renderer::new(&self.dimensions, self.scale)?;
        let mut i = 0;
        // let actions = vec![
        //     Some(GameEvent::PlayPause),
        //     Some(GameEvent::Up),
        //     None,
        //     None,
        //     None,
        //     None,
        //     Some(GameEvent::Left),
        //     None,
        //     None,
        //     Some(GameEvent::Quit),
        // ];
        loop {
            println!("Frame {i}; scene={:?}", state.scene);
            let input: Option<GameEvent> = renderer.get_input();
            eprintln!("input: {input:?}");
            // let user_input = actions[i];
            if let Some(ev) = input {
                eprintln!("{ev:?}");
                match ev {
                    GameEvent::Quit => break Ok(()),
                    GameEvent::PlayPause => state.toggle_playpause(),
                    _ => (),
                }
            }
            // sleep(Duration::from_millis(self.frame_rate));
            let direction = input.map(|ev| ev.to_direction()).flatten();
            self.step(&mut state, &mut renderer, direction);
            i += 1;
            renderer.update();
            sleep(Duration::from_millis(self.frame_rate));
            renderer.clear();
        }
    }
}
