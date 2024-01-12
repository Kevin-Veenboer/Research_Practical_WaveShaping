import numpy as np


def generate_grid():
    # Grid parameters
    centre = (614, 610)
    distance = 160
    angle = 45
    angle_rad = -(angle / 180) * np.pi
    grid_number = 5

    # Determine x and y steps
    grid_array_x = np.array(range(grid_number))[::-1] - 2
    grid_array_y = np.copy(grid_array_x)

    # make step matrix
    grid_matrix = np.array(
        [
            [
                (
                    round(step_x * distance),
                    round(step_y * distance),
                )
                for step_x in grid_array_x
            ]
            for step_y in grid_array_y
        ]
    )

    print(grid_matrix)

    # Determine rotation matrix
    rotation = np.array(
        [
            (np.cos(angle_rad), -np.sin(angle_rad)),
            (np.sin(angle_rad), np.cos(angle_rad)),
        ]
    )

    coord_grid_relative = np.array(
        [
            np.matmul(rotation, element)
            for element in grid_matrix.reshape(grid_number**2, 2)
        ]
    )

    coord_grid = np.array(
        [
            (centre[0] + offset[0], centre[1] + offset[1])
            for offset in coord_grid_relative
        ]
    )

    return [tuple(element) for element in coord_grid.round(decimals=0).astype(int)]


def main():
    grid = generate_grid()
    for element in grid:
        print(tuple(element))


if __name__ == "__main__":
    main()
