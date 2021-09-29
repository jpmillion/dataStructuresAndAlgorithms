def depthFirstSearch(node, v, visited = {}):

    stack = [node]

    while len(stack):
        curr = stack.pop()

        print(curr.value)

        if curr.value == v:
            return True

        visited[curr.value] = True

        for child in curr.children:
            if child.value in visited:
                continue

            stack.append(child)

    return False
