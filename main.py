# def monotone(array):
#     decreasing = increasing = True
#     for i in range(1, len(array)):
#         if array[i] > array[i - 1]:
#             decreasing = False
#             continue
#         if array[i] < array[i - 1]:
#             increasing = False
#             continue
#         # if array[i] == array[i - 1]:
#         #     decreasing = False
#     return decreasing or increasing

def monotone(array):
    ask = desk = True
    for i in range(0, len(array) - 1):

        if array[i + 1] > array[i] and ask:
            desk = False
            continue

        if array[i + 1] < array[i] and desk:
            ask = True
            continue

        if array[i + 1] < array[i] and ask:
            return False

        if array[i + 1] > array[i] and desk:
            return False

    return True
