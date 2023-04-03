import random

def generate_non_repeating_random_numbers_2d_list(rows: int, cols: int):
    numbers = [i for i in range(1, rows * cols + 1)]
    random_numbers = []
    for i in range(rows):
        random_numbers.append([])
        for j in range(cols):
            rand_num = random.choice(numbers)
            random_numbers[i].append(rand_num)
            numbers.remove(rand_num)
    return random_numbers