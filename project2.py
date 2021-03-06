"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1: Amy Wang (pw137)
Partner 2: Lu Liu (ll394)
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    #build DFS    
    if alg == 'DFS':
    #initialize all values
        path = []
        for v in maze.adjList:
            v.visited = False
            v.prev = None
        stack = Stack()
    #mark the start vertex as visited and push it onto the stack
        maze.start.visited = True
        stack.push(maze.start)
    #loop while the stack is not empty
        while not stack.isEmpty():
            current = stack.pop()
    #if reach exist, break
            if current == maze.exit:
    #find path
                while current is not None:
                    path.append(current.rank)
                    current = current.prev
                break
    #check neighbors,mark itn and push it onto stack.
            for v in current.neigh:
                if v.visited is False:
                    v.visited = True
                    stack.push(v)
                    v.prev = current

    
    #build BFS
    if alg == 'BFS':
    #initialize all values
        path = []
        for v in maze.adjList:
            v.visited = False
            v.prev = None
    #push the start vertex into the queue and set it distance = 0
    #queue.push(maze.start)
        queue = Queue()
        maze.start.visited = True
        queue.push(maze.start)
    #obtain the current vertex
        while not queue.isEmpty():
            current = queue.pop()
    #if reach exist,break
            if current == maze.exit:
    #find path
                while current is not None:

                    path.append(current.rank)
                    current = current.prev
                break
    #push the neighbour into the queue if they have not yet been visited
            for v in current.neigh:
                if v.visited is False:
                    v.visited = True
                    queue.push(v)
                    v.prev = current
    #reverse path to get the correct order
    path.reverse()
    return path

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
