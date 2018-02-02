def set_current_node(visited, distances):
    """Returns the node that should be set as current node.
    visited -- set that contains the nodes marked as visited
    distances -- dictionary mapping each node to its current distance
    """
    min_distance = 100
    current_node = ""
    for (node, distance) in distances.items():
        if (node not in visited and distance < min_distance):
            min_distance = distance
            current_node = node

    return current_node
