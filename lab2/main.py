import math


def min_square_size(N, W, H):
    if not (1 <= N <= 1012 and 1 <= W <= 109 and 1 <= H <= 109):
        return -1, -1

    max_leaf_size = max(W, H)
    min_board_size = max_leaf_size
    while True:
        rows = math.floor(min_board_size / H)
        cols = math.floor(min_board_size / W)
        total_leaves = rows * cols

        if total_leaves >= N:
            break

        min_board_size += 1

    return min_board_size


N, W, H = map(int, input().split())

result = min_square_size(N, W, H)
print(result)


# N = 2
# W = 1000000000
# H = 999999999

# N = 10
# W = 2
# H = 3

# N = 4
# W = 1
# H = 1
