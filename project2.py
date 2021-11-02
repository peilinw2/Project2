"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1:
Partner 2:
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
        
    if alg == 'DFS':
    #initialize all values
        path = []
        for v in maze.adjust:
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
    
    
    
    return []
    if alg == 'BFS':
          path =()
    #Initialize all values
          for v in maze.adjList
          v.dist = False
          v.prev = None

    queue = Queue()
    #Push the start vertex into the queue and set it distance = 0
    queue.push(maze.start)
    maze.start.dist = 0

    #Obtain the current vertex
    While not queue.isEmpty():
        Current = queue.pop()
        if current.rank == maze.exit.rank:
            if current.is Equal(maze.exit):
                break
                 #push the neighbour into the queue if they have not yet been visited
            for v in current.neigh:
                if v.dist == False:
                    v.dist = current.dist + 1
                    queue.push(v)
                    v.prev = current

              

    
    

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
