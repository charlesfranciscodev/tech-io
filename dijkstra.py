def set_current_node(visited, currentDistances):
    # visited is a set that contains the names of the nodes marked as visited.
    # currentDistances is a dictionary that contains the current minimum distance of each node.
    min_distance = 100
    current_node = ""
    for (node, distance) in currentDistances.items():
      if (node not in visited and distance < min_distance):
        min_distance = distance
        current_node = node

    return current_node
