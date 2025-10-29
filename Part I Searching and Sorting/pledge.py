# this code is generated using chatGPT 

# Directions in order: NORTH, EAST, SOUTH, WEST
DIRECTIONS = [(-1,0), (0,1), (1,0), (0,-1)]
NORTH, EAST, SOUTH, WEST = 0,1,2,3

def turn_left(direction):
    return (direction - 1) % 4

def turn_right(direction):
    return (direction + 1) % 4

def is_free_cell(grid, row, col):
    try:
        return grid[row][col] == 0
    except IndexError:
        return False

    return grid[row][col] == 0

def pledge_algorithm(grid, start_row, start_col):
    row, col = start_row, start_col
    heading = EAST                  # target heading = east
    turn_angle_sum = 0
    path_taken = [(row, col)]

    def try_step_forward(direction, r, c):
        """Try to advance one cell in 'direction' from (r,c)."""
        nr = r + DIRECTIONS[direction][0]
        nc = c + DIRECTIONS[direction][1]
        if is_free_cell(grid, nr, nc):
            return nr, nc, True
        return r, c, False

    # exit condition: reaching the rightmost column
    while col < len(grid[0]) - 1:
        next_r, next_c, can_move = try_step_forward(heading, row, col)

        # if we are not currently wall-following (turn_angle_sum==0)
        # then simply walk straight if possible
        if can_move and turn_angle_sum == 0:
            row, col = next_r, next_c
            path_taken.append((row, col))
            continue

        # ---- wall following phase ----
        # step 1) turn right once and account for it
        heading = turn_right(heading)
        turn_angle_sum += 90

        # step 2) follow the wall
        while True:
            # if blocked forward → turn left and subtract angle
            forward_r, forward_c, can_go_forward = try_step_forward(heading, row, col)
            if not can_go_forward:
                heading = turn_left(heading)
                turn_angle_sum -= 90
                continue

            # else move forward
            row, col = forward_r, forward_c
            path_taken.append((row, col))

            # stop wall-following iff
            #   (1) angle sum is back to zero
            #   (2) heading is original target direction
            if turn_angle_sum == 0 and heading == EAST:
                break

    return path_taken


# ---- EXAMPLE GRID ----
grid = [
 [0,0,0,0,0,0,0],
 [0,1,1,0,1,1,0],
 [0,0,0,0,0,0,0],
 [0,1,1,1,1,1,0],
 [0,0,0,0,0,0,0],
]

path = pledge_algorithm(grid, 2, 0)
print(path)
