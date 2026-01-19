# differences in impl from py
after implementing it in python, i have a better understanding of the do's and dont's, and a better understanding of the pipeline.

`input -> engine logic -> (cartesian) -> *scale -> (raster) -> renderer -> sdl -> update`
as the engine logic is pure i should be able to directly translate it into rust. however a big issue in python seemed to be translating the cartesian space into raster space, the entire conversion is just `(x+X/2,y+Y/2) where (X,Y) = screenDimensions`.

the games state is stored in `State`, the most important being `State.scene`, the step function will match based on the `Scene` enum. 

when no input is given, the snake uses the last given input to move, in the py impl this was a mess, and ultimately was managed by `Snake`. 
i would prefer a less crude way to use the last given input. i dont want hidden state in the Snake. so originally it was in the `Input` class. but again it was a mess.
the best solution would probably be to store last_direction in State. and give it a set_direction function which takes in the `Key` enum. this is where all the direction logic goes. in which case the state definition should be within engine.
will_grow will also be moved outside of snake and into state.

another stupid thing was that it rendered the entire board into a coordinate system, most of which were empty tiles.
something much more efficient would just be to ship just a vector of the units, since it uses the embedded coordinates to render its position anyways.

in python, initially engine was the stateful object, but then it would return a large supertuple of evaluated flags, which i encapsulated in `State`, but then that meant that there were two stateful objects, three if you count `Snake`. so I will be reorganizing board into State, with the `Board.evaluate_state` method being remapped to `State.evaluate` which returns the coordinates to be rendered, but mutates its state with the new evaluation
