# from itertools import combinations
#
#
# def min_beers(N, B, likes):
#
#     all_combinations = []
#     for r in range(1, B+1):
#         all_combinations.extend(combinations(range(B), r))
#
#     for combo in sorted(all_combinations, key=len):
#         if all(any(likes[i][beer] == 'Y' for beer in combo) for i in range(N)):
#             return len(combo)
#
#
# def read_input(filename):
#     with open(filename, 'r') as file:
#         N, B = map(int, file.readline().split())
#         likes = [file.readline().strip() for _ in range(N)]
#     return N, B, likes
#
# def write_output(filename, result):
#     with open(filename, 'w') as file:
#         file.write(str(result) + '\n')
#
# if __name__ == "__main__":
#     input_file = "beer.in"
#     output_file = "beer.out"
#
#     N, B, likes = read_input(input_file)
#     result = min_beers(N, B, likes)
#     write_output(output_file, result)

from collections import deque
from itertools import combinations

def min_beers(N, B, likes):

    queue = deque([set()])
    while queue:

        combo = queue.popleft()

        if all(any(likes[i][beer] == 'Y' for beer in combo) for i in range(N)):
            return len(combo)
       
        for beer in range(B):
            if beer not in combo:
                queue.append(combo | {beer})

def read_input(filename):
    with open(filename, 'r') as file:
        N, B = map(int, file.readline().split())
        likes = [file.readline().strip() for _ in range(N)]
    return N, B, likes

def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result) + '\n')

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    N, B, likes = read_input(input_file)
    result = min_beers(N, B, likes)
    write_output(output_file, result)
