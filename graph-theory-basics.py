def get_graph_info(adj_list):
    """return: maximum grade of a node,
    number of loops,
    boolean representing if there are parallel edges.
    """
    grades = {}
    loops = 0
    parallel_edges = False
    for i, edge in enumerate(adj_list):
        for node in edge:
            if node in grades:
                grades[node] += 1
            else:
                grades[node] = 1

        if (edge[0] == edge[1]):
            loops += 1
        if (not parallel_edges):
            for j in range(i + 1, len(adj_list)):
                other_edge = adj_list[j]
                if (edge == other_edge or edge[::-1] == other_edge):
                    parallel_edges = True
    return max(grades.values()), loops, parallel_edges
