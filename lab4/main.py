from collections import deque


def has_cycle(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if is_cyclic(node, graph, visited):
                return True
    return False


def is_cyclic(node, graph, visited):
    queue = deque()
    queue.append((node, -1))

    while queue:
        current, parent = queue.popleft()
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor != parent:
                if neighbor in visited:
                    return True
                queue.append((neighbor, current))

    return False


def main():
    with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
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

        result = has_cycle(graph)
        output_file.write(str(result))


if __name__ == "__main__":
    main()
