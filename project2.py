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
    ##### Your implementation goes here. #####
    
    

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
