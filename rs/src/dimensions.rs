use rand::Rng;

pub type LogicalCoordinate = (isize, isize);
pub type ScreenCoordinates = (usize, usize);

#[derive(Debug, Clone)]
pub struct Dimensions {
    xmin: isize,
    xmax: isize,
    ymin: isize,
    ymax: isize,
    abs: ScreenCoordinates,
    scale: isize,
}
impl Dimensions {
    pub fn new((x, y): ScreenCoordinates, scale: usize) -> Self {
        let (dx, dy) = ((x / 2) as isize, (y / 2) as isize);

        Self {
            xmin: -dx,
            xmax: dx,
            ymin: -dy,
            ymax: dy,
            abs: (x, y),
            scale: scale as isize,
        }
    }
    pub fn bounds(&self) -> (LogicalCoordinate, LogicalCoordinate) {
        ((self.xmin, self.xmax), (self.ymin, self.ymax))
    }

    pub fn out_of_bounds(&self, (x, y): LogicalCoordinate) -> bool {
        x < self.xmin*2/self.scale || x > self.xmax*2/self.scale || y < self.ymin*2/self.scale || y > self.ymax*2/self.scale
    }

    pub fn to_screen(&self, (x, y): LogicalCoordinate) -> ScreenCoordinates {
        /// if x is less than 0, return 0
        fn saturating_cast(x: isize) -> usize {
            if x < 0 { 0 } else { x as usize }
        }
        // ((x + self.xmax) as usize, (self.ymax - y) as usize)
        // if x' is negative it causes the usize cast to wrap around
        (
            saturating_cast(x + self.xmax),
            saturating_cast(self.ymax - y),
        )
    }

    pub fn to_logical(&self, (x, y): ScreenCoordinates) -> LogicalCoordinate {
        ((x as isize - self.xmax), (y as isize - self.ymax))
    }
    /// returns a random coordinate
    pub fn random(&self) -> LogicalCoordinate {
        let mut rng = rand::rng();
        (
            rng.random_range((self.xmin*2/ self.scale) as i32..=(self.xmax*2/ self.scale) as i32)
                as isize,
            rng.random_range((self.ymin*2/ self.scale) as i32..=(self.ymax*2/ self.scale) as i32)
                as isize,
        )
    }
    pub fn get_screen_bounds(&self) -> ScreenCoordinates {
        self.abs
    }
}
