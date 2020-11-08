from typing import NamedTuple
from graph_util import *
from math import inf
import queue

def shortest(roadmap, elevations, start, end):
    """
    Returns the length of the shortest highroad-lowroad path.
    The input is the graph of cities, a dictionary mapping cities to elevations, the start node and the end node.
    
    We basically want to perform breadth-first search to find the shortest.
    """
    return algorithm(roadmap, elevations, start, end)[0]


def num_shortest(roadmap, elevations, start, end):
    """
    Returns the number of shortest highroad-lowroad paths
    The input is the graph of cities, a dictionary mapping cities to elevations, the start node and the end node.
    """
    return algorithm(roadmap, elevations, start, end)[1]

def algorithm(roadmap, elevations, start, end):    
    num_ways = {} # will represent the number of ways to get to an outcome
    moves = {} # will represent the number of moves to reach a node

    for node in roadmap.get_nodes():
        for node2 in roadmap.get_nodes():
            moves[node+node2] = inf # we want min number of moves, so set initially to infinity
            num_ways[node+node2] = -inf # we want max number of moves, set initially to -inifity

    moves[start+start] = 0 # 0 moves from start to start
    num_ways[start+start] = 1 # 1 way to get from start to start

    q = queue.Queue() # create queue and enqueue the starting pair
    q.put((start, start))

    while not q.empty():
        # grab the top pair on the stack
        low, high = q.get()

        current_moves = moves[low+high] # get the current values from the moves and num ways dictionaries
        current_num_ways = num_ways[low+high]

        # can we move the high node?
        for adj in roadmap.get_neighbors(high):
            # is it a valid move?
            if elevations[adj] > elevations[low]:
                # have we solved this / does it make sense to continue
                if current_moves + 1 < moves[low+adj]: # we have a new best way to get to a node
                    moves[low+adj] = current_moves + 1 # reflect the number of moves and ways to reflect
                    num_ways[low+adj] = current_num_ways
                    q.put((low, adj)) # enqueue this pair, we need to solve again
                elif current_moves + 1 == moves[low+adj]: # we have found more ways to get the same outcome, update numways to reflect
                    num_ways[low+adj] += current_num_ways
            elif adj == low and adj == end: # so we have not found an eligble node, unless the node we are attempting to is the end node, in which case the usual rules of moving do not apply, we can end up at the same node
                if current_moves + 1 < moves[end+end]: # we have found a new best way to reach the end node, update numways and moves to reflect
                    num_ways[end+end] = current_num_ways
                    moves[end+end] = current_moves + 1
                elif current_moves + 1 == moves[end+end]: # we have found an equally good way to find the end node, update numways to reflect
                    num_ways[end+end] += current_num_ways

        # can we move the low node?
        for adj in roadmap.get_neighbors(low):
            # is it a valid move?
            if elevations[adj] < elevations[high]:
                # have we solved this / does it make sense to continue
                if current_moves + 1 < moves[adj+high]:
                    moves[adj+high] = current_moves + 1
                    num_ways[adj+high] = current_num_ways
                    q.put((adj, high))
                elif current_moves + 1 == moves[adj+high]:
                    num_ways[adj+high] += current_num_ways
            elif adj == high and adj == end:
                if current_moves + 1 < moves[end+end]:
                    num_ways[end+end] = current_num_ways
                    moves[end+end] = current_moves + 1
                elif current_moves + 1 == moves[end+end]:
                    num_ways[end+end] += current_num_ways

        # can we move both low and high?
        for adj_high in roadmap.get_neighbors(high):
            for adj_low in roadmap.get_neighbors(low):
                if elevations[adj_high] > elevations[adj_low]:
                    if current_moves + 1 < moves[adj_low+adj_high]:
                        moves[adj_low+adj_high] = current_moves + 1
                        num_ways[adj_low+adj_high] = current_num_ways
                        q.put((adj_low, adj_high))
                    elif current_moves + 1 == moves[adj_low+adj_high]:
                        num_ways[adj_low+adj_high] += current_num_ways
                elif adj_high == adj_low and adj_high == end:
                    if current_moves + 1 < moves[end+end]:
                        num_ways[end+end] = current_num_ways
                        moves[end+end] = current_moves + 1
                    elif current_moves + 1 == moves[end+end]:
                        num_ways[end+end] += current_num_ways
    return moves[end+end], num_ways[end+end]