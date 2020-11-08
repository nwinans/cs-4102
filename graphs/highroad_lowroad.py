from graph_util import *
from math import inf
import queue

def shortest(roadmap, elevations, start, end):
    """
    Returns the length of the shortest highroad-lowroad path.
    The input is the graph of cities, a dictionary mapping cities to elevations, the start node and the end node.
    
    We basically want to perform breadth-first search to find the shortest.
    """

    low_shortest_visited = { key:inf for key in roadmap.get_nodes() }
    high_shortest_visited = { key:inf for key in roadmap.get_nodes() }

    low_shortest_visited[start] = 0
    high_shortest_visited[start] = 0

    matches = []

    q = queue.Queue()
    q.put((start, start))

    while not q.empty():
        # grab the top pair on the stack
        low, high = q.get()
        #print(f"(low, high) = ({low}, {high})")
        # are we at the end?, we want to reach the end at the same time so break if one is there
        if low == end and high == end:
            print(f'Other method - Apparently at end -- high {high_shortest_visited[high]}, low {low_shortest_visited[low]}')
            continue

        high_current = high_shortest_visited[high]
        low_current = low_shortest_visited[low]

        # can we move the high node?
        for adj in roadmap.get_neighbors(high):
            # is it a valid move?
            if elevations[adj] > elevations[low]:
                # have we solved this / does it make sense to continue
                if high_current + 1 < high_shortest_visited[adj]:
                    high_shortest_visited[adj] = high_current + 1
                    q.put((low, adj))
            elif adj == low and adj == end:
                print(f'High moved - Apparently at end -- high {high_shortest_visited[high]}, low {low_shortest_visited[low]}')
                high_shortest_visited[adj] = min(high_current + 1, high_shortest_visited[adj])
                matches.append(high_current + 1)

        # can we move the low node?
        for adj in roadmap.get_neighbors(low):
            # is it a valid move?
            if elevations[adj] < elevations[high]:
                # have we solved this / does it make sense to continue
                if low_current + 1 < low_shortest_visited[adj]:
                    low_shortest_visited[adj] = low_current + 1
                    q.put((adj, high))
            elif adj == high and adj == end:
                print(f'Low moved - Apparently at end -- high {high_shortest_visited[high]}, low {low_shortest_visited[low]}')
                low_shortest_visited[adj] = min(low_current + 1, low_shortest_visited[adj])
                matches.append(low_current + 1)


        # can we move both low and high?
        for adj_high in roadmap.get_neighbors(high):
            for adj_low in roadmap.get_neighbors(low):
                if elevations[adj_high] > elevations[adj_low]:
                    if low_current + 1 < low_shortest_visited[adj_low] or high_current + 1 < high_shortest_visited[adj_high]:
                        low_shortest_visited[adj_low] = min(low_current + 1, low_shortest_visited[adj_low])
                        high_shortest_visited[adj_high] = min(high_current + 1, high_shortest_visited[adj_high])
                        q.put((adj_low, adj_high))
                elif adj_high == adj_low and adj_high == end:
                    print(f'Both moved - Apparently at end -- high {high_shortest_visited[high]}, low {low_shortest_visited[low]}')
                    low_shortest_visited[adj_low] = min(low_current + 1, low_shortest_visited[adj_low])
                    high_shortest_visited[adj_high] = min(high_current + 1, high_shortest_visited[adj_high])
                    matches.append(max(low_current + 1, high_current + 1))

    print(matches)

    return max(high_shortest_visited[end], low_shortest_visited[end])

def num_shortest(roadmap, elevations, start, end):
    """
    Returns the number of shortest highroad-lowroad paths
    The input is the graph of cities, a dictionary mapping cities to elevations, the start node and the end node.
    """
    return 0

def num_shortest_helper(roadmap, elevations, start, end, current):
    if low is end and high is end:
        return 1
    