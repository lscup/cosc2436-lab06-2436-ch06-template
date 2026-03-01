"""
Lab 6: Breadth-First Search Implementation
Finds shortest path (by number of edges) in unweighted graph.
"""
from typing import List, Dict, Optional
from collections import deque
from graph import Graph

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        List of vertices forming the path, or None if no path exists
    """
    if start not in graph.vertices or end not in graph.vertices:
        print(f"Error: '{start}' or '{end}' not in graph")
        return None
    
    # Queue stores (current_vertex, path_to_current)
    queue = deque([(start, [start])])
    
    # Track visited vertices to avoid cycles
    visited = {start}
    
    print(f"\nBFS from '{start}' to '{end}':")
    print("-" * 40)
    
    level = 0
    nodes_at_level = 1
    next_level_nodes = 0
    
    while queue:
        current, path = queue.popleft()
        nodes_at_level -= 1
        
        print(f"Level {level}: Visiting '{current}'")
        
        # Found the destination!
        if current == end:
            print(f"\nFound path with {len(path) - 1} edges!")
            return path
        
        # Explore neighbors
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                next_level_nodes += 1
        
        # Track levels for visualization
        if nodes_at_level == 0:
            level += 1
            nodes_at_level = next_level_nodes
            next_level_nodes = 0
    
    print(f"\nNo path found from '{start}' to '{end}'")
    return None

def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    """
    Find all vertices reachable from start and their distances.
    
    Returns:
        Dict mapping vertex -> distance from start
    """
    if start not in graph.vertices:
        return {}
    
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        current_dist = distances[current]
        
        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)
    
    return distances

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    path = bfs_find_path(graph, v1, v2)
    return path is not None
