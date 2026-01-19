use std::collections::HashSet;
pub enum TileType {
    Snake,
    Apple,
    Null,
}
pub type EvaluatedState = Vec<(CartesianCoordinate, TileType)>;
pub type CartesianCoordinate = (isize, isize);
pub type RasterCoordinate = (usize, usize);

pub enum Direction {
    Up,
    Down,
    Left,
    Right,
}
pub enum Scene {
    Start,
    Paused,
    Playing,
    Dead,
}
pub struct Dimensions {
    xmin: isize,
    xmax: isize,
    ymin: isize,
    ymax: isize,
    abs: CartesianCoordinate,
}
impl Dimensions {
    pub fn new((x, y): CartesianCoordinate) -> Self {
        let (dx, dy) = (x / 2, y / 2);

        Self {
            xmin: -dx,
            xmax: dx,
            ymin: -dy,
            ymax: dy,
            abs: (x, y),
        }
    }
    pub fn bounds(&self) -> (CartesianCoordinate, CartesianCoordinate) {
        ((self.xmin, self.xmax), (self.ymin, self.ymax))
    }

    pub fn out_of_bounds(&self, (x, y): CartesianCoordinate) -> bool {
        x < self.xmin || x > self.xmax || y < self.ymin || x > self.ymax
    }

    pub fn to_raster(&self, (x, y): CartesianCoordinate) -> RasterCoordinate {
        ((x + self.xmax) as usize, (y + self.ymax) as usize)
    }

    pub fn to_cartesian(&self, (x, y): RasterCoordinate) -> CartesianCoordinate {
        ((x as isize - self.xmax), (y as isize - self.ymax))
    }
    /// returns a random coordinate
    pub fn random(&self) -> CartesianCoordinate {
        todo!()
    }
}
pub struct State {
    will_grow: bool,
    direction: Option<Direction>,
    apples_ate: usize,
    apple_position: CartesianCoordinate,
    snake: Snake,
    dimensions: Dimensions,
    scene: Scene,
}
impl State {
    pub fn evaluate(&mut self, direction: Option<Direction>) -> EvaluatedState {
        self.move_snake(direction);
        if self.ate_apple() {
            self.will_grow = true;
            self.spawn_apple();
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
    fn get_adjacent_apple_coordinates(&self) -> Vec<CartesianCoordinate> {
        let (ax, ay) = self.apple_position;
        (-1..=1)
            .into_iter()
            .map(|y| (-1..=1).into_iter().map(move |x| (x + ax, y + ay)))
            .flatten()
            .collect()
    }
    fn move_snake(&mut self, direction: Option<Direction>) {
        if let Some(d) = &direction {
            self.snake.advance(self.will_grow, d);
        } else if let Some(ld) = &self.direction {
            self.snake.advance(self.will_grow, ld);
        } else {
            () // expliciting doing nothing
        }
    }
    fn ate_apple(&self) -> bool {
        *self.snake.get_head() == self.apple_position
    }
}
// struct CoordinateSpace<T> {
//     dimensions: Dimensions,
//     space: Vec<Vec<T>>,
// }
// impl<T> CoordinateSpace<T> {
//     fn get_cartesian(&self, cartesian: CartesianCoordinate) -> Option<&T> {
//         self.get_raster(self.dimensions.to_raster(cartesian))
//     }
//     fn set_cartesian(&mut self, cartesian: CartesianCoordinate, value: T) {
//         self.set_raster(self.dimensions.to_raster(cartesian), value);
//     }

//     fn get_raster(&self, (x, y): RasterCoordinate) -> Option<&T> {
//         self.space.get(y).and_then(|xs| xs.get(x))
//     }

//     fn set_raster(&mut self, (x, y): RasterCoordinate, value: T) {
//         self.space
//             .get_mut(y)
//             .and_then(|xs| xs.get_mut(x))
//             .and_then(|v| Some(*v = value));
//     }
// }

struct Snake {
    segments: Vec<CartesianCoordinate>,
}
impl Snake {
    fn initial() -> Vec<CartesianCoordinate> {
        vec![(0, 0), (1, 0), (2, 0)]
    }
    fn new() -> Self {
        Self {
            segments: Self::initial(),
        }
    }
    fn reset(&mut self) {
        self.segments = Self::initial()
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
    fn get_head(&self) -> &CartesianCoordinate {
        self.segments.last().unwrap()
    }
    fn add_head(&mut self, head: CartesianCoordinate) {
        self.segments.push(head);
    }
    fn remove_tail(&mut self) {
        self.segments.remove(0);
    }
    fn advance(&mut self, will_grow: bool, direction: &Direction) {
        self.move_head(direction);
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
