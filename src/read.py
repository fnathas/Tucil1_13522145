from collections import deque

def read_file(file: str) -> tuple[int, int, int, list[list[str]], int, list[list[str]], list[int]]:
    with open("test/" + file, "r") as f:
        lines = f.readlines()

    buffer_size = int(lines[0].strip())
    matrix_width, matrix_height = map(int, lines[1].strip().split())
    matrix = [list(map(str, line.strip().split())) for line in lines[2:2+matrix_height]]
    number_of_sequences = int(lines[2+matrix_height].strip())

    sequences = []
    rewards = []
    for i in range(number_of_sequences):
        sequences.append(list(map(str, lines[3+matrix_height+i*2].strip().split())))
        rewards.append(int(lines[4+matrix_height+i*2].strip()))

    return buffer_size, matrix_width, matrix_height, matrix, number_of_sequences, sequences, rewards

def generate_strict_combinations(matrix, step):
    rows, cols = len(matrix), len(matrix[0])
    all_paths = []

    # Queue for the paths to explore, each entry is a tuple with the current path and the remaining steps
    queue = deque(
        ([(matrix[0][x], (x, 0))], step - 1, "vertical", {(x, 0)})
        for x in range(cols)
    )

    while queue:
        path, steps, direction, visited = queue.popleft()

        if steps == 0:
            all_paths.append(path)
            continue

        x, y = path[-1][1]

        if direction == "vertical":
            for next_y in range(rows):
                if (x, next_y) not in visited:
                    queue.append(
                        (
                            path + [(matrix[next_y][x], (x, next_y))],
                            steps - 1,
                            "horizontal",
                            visited | {(x, next_y)},
                        )
                    )
        else:  # horizontal
            for next_x in range(cols):
                if (next_x, y) not in visited:
                    queue.append(
                        (
                            path + [(matrix[y][next_x], (next_x, y))],
                            steps - 1,
                            "vertical",
                            visited | {(next_x, y)},
                        )
                    )

    return all_paths

def compare_path_with_sequence(
    path: list[tuple[str, tuple[int, int]]], sequence: list[str],
) -> bool:
    for i in range(0, len(path)-len(sequence)+1):
        if all(path[i+j][0] == sequence[j] for j in range(len(sequence))):
            return True
    return False

def compare_paths(
    all_paths: list[list[tuple[str, tuple[int, int]]]],
    sequences: list[list[str]],
    rewards: list[int],
) -> tuple[list[list[tuple[str, tuple[int, int]]]], int]:
    result = []
    point = 0
    temp = 0
    for path in all_paths:
        for i in range(len(sequences)):
            if compare_path_with_sequence(path, sequences[i]):
                point += rewards[i]
        if (len(result) == 0):
            result = path
            temp = point
        else:
            if (point > temp):
                result = path
                temp = point
        point = 0
    
    return result, temp