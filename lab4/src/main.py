from collections import deque


def has_cycle(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if is_cyclic(node, graph, visited, parent=None):
                return "True"
    return "False"


def is_cyclic(node, graph, visited, parent):
    queue = deque()
    queue.append((node, parent))

    while queue:
        current, parent = queue.popleft()
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor != parent:
                if neighbor in visited:
                    return True
                queue.append((neighbor, current))

    return False


def read_graf_from_file():
    with open("input.txt", "r") as input_file:
        graph = {}
        lines = input_file.readlines()
        for line in lines:
            u, v = map(int, line.split())
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

    return graph


def write_result(result):
    with open("output.txt", "w") as output_file:
        output_file.write(result)


def main():
    graph = read_graf_from_file()
    result = has_cycle(graph)
    write_result(result)


if __name__ == "__main__":
    main()

