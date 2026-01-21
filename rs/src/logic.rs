use rand::prelude::*;
use std::collections::HashSet;

use crate::dimensions::{Dimensions, LogicalCoordinate};
pub enum TileType {
    Snake,
    Apple,
}
pub type EvaluatedState = Vec<(LogicalCoordinate, TileType)>;

#[derive(Clone, Debug, Copy)]
pub enum Direction {
    Up,
    Down,
    Left,
    Right,
}
impl Direction {
    pub fn is_opposite(&self, other: &Self) -> bool {
        match (self, other) {
            (Direction::Up, Direction::Down) => true,
            (Direction::Down, Direction::Up) => true,
            (Direction::Left, Direction::Right) => true,
            (Direction::Right, Direction::Left) => true,
            _ => false,
        }
    }
    fn filter_opposite(&self, other: &Self) -> Option<&Self> {
        if self.is_opposite(other) {
            None
        } else {
            Some(&self)
        }
    }
}
#[derive(Clone, Copy, Debug)]
pub enum Scene {
    Start,
    Paused,
    Playing,
    Dead,
}

pub struct State {
    pub will_grow: bool,
    pub last_direction: Option<Direction>,
    pub apples_ate: usize,
    pub apple_position: LogicalCoordinate,
    pub snake: Snake,
    pub dimensions: Dimensions,
    pub scene: Scene,
    pub score: usize,
}
impl State {
    pub fn new(dimensions: &Dimensions) -> Self {
        let mut state = Self {
            will_grow: false,
            last_direction: None,
            apples_ate: 0,
            apple_position: (0, 0),
            snake: Snake::new(),
            dimensions: dimensions.clone(),
            scene: Scene::Start,
            score: 0,
        };
        state.spawn_apple();
        state
    }
    pub fn evaluate(&mut self, direction: &Option<Direction>) -> EvaluatedState {
        // check if direction is Some, check if its opposite, if opposite return None, if not Some return None,
        // if last direction was None then return direction
        let filtered_direction = if let Some(current_direction) = direction {
            if let Some(last_direction) = self.last_direction.clone() {
                if !current_direction.is_opposite(&last_direction) {
                    self.last_direction = direction.clone();
                    direction
                } else {
                    &self.last_direction.clone()
                }
            } else {
                self.last_direction = direction.clone();
                eprintln!("--- SETTING LAST DIRECTION TO {direction:?}");
                direction
            }
        } else {
            &self.last_direction.clone()
        };
        self.move_snake(filtered_direction);
        self.will_grow = false;
        if self.ate_apple() {
            self.score += 1;
            self.will_grow = true;
            eprintln!("ate apple! score={}", self.score);
            self.spawn_apple();
        }
        if self.snake.collision(&self.dimensions) {
            self.scene = Scene::Dead;
            eprintln!("You Died!");
        }
        let mut evaluated: EvaluatedState = self
            .snake
            .segments
            .clone()
            .iter()
            .map(|seg| (*seg, TileType::Snake))
            .collect();
        evaluated.push((self.apple_position, TileType::Apple));
        evaluated
    }

    pub fn toggle_playpause(&mut self) {
        self.scene = match self.scene {
            Scene::Start => Scene::Playing,
            Scene::Paused => Scene::Playing,
            Scene::Playing => Scene::Paused,
            Scene::Dead => Scene::Playing,
            _ => self.scene,
        };
        println!("toggled scene to {:?}", self.scene)
    }
    fn spawn_apple(&mut self) {
        // let unavailable_coordinates = vec![self.apple_position].append(self.snake.segments.clone());
        let mut unavailable_coordinates = self.snake.segments.clone();
        unavailable_coordinates.append(&mut self.get_adjacent_apple_coordinates());
        self.apple_position = loop {
            let rand = self.dimensions.random();
            if !unavailable_coordinates.contains(&rand) {
                break rand;
            }
        }
    }
    fn get_adjacent_apple_coordinates(&self) -> Vec<LogicalCoordinate> {
        let (ax, ay) = self.apple_position;
        (-1..=1)
            .into_iter()
            .map(|y| (-1..=1).into_iter().map(move |x| (x + ax, y + ay)))
            .flatten()
            .collect()
    }
    fn move_snake(&mut self, direction: &Option<Direction>) {
        if let Some(d) = direction {
            self.snake.advance(self.will_grow, d);
        }
    }
    fn ate_apple(&self) -> bool {
        *self.snake.get_head() == self.apple_position
    }
}

pub struct Snake {
    segments: Vec<LogicalCoordinate>,
}
impl Snake {
    fn new() -> Self {
        Self {
            segments: vec![(0, 0), (1, 0), (2, 0)],
        }
    }
    fn move_head(&mut self, direction: &Direction) {
        let (hx, hy) = self.get_head();
        let new_head = match direction {
            Direction::Up => (*hx, *hy + 1),
            Direction::Down => (*hx, *hy - 1),
            Direction::Left => (*hx - 1, *hy),
            Direction::Right => (*hx + 1, *hy),
        };
        self.add_head(new_head);
    }
    fn get_head(&self) -> &LogicalCoordinate {
        self.segments.last().unwrap()
    }
    fn add_head(&mut self, head: LogicalCoordinate) {
        self.segments.push(head);
    }
    fn remove_tail(&mut self) {
        self.segments.remove(0);
    }
    fn advance(&mut self, will_grow: bool, direction: &Direction) {
        self.move_head(direction);
        eprintln!("moving snake {direction:?}");
        if !will_grow {
            self.remove_tail();
        }
    }
    fn collision(&self, dimensions: &Dimensions) -> bool {
        let wall_coll = self
            .segments
            .iter()
            .map(|seg| dimensions.out_of_bounds(*seg))
            .any(|t| t);
        let self_coll = {
            let mut uniq = HashSet::new();
            !self.segments.iter().all(|x| uniq.insert(x))
        };
        wall_coll || self_coll
    }
}
