# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    explored_nodes = [] #maintaining tuple of immutable expanded nodes
    action_seq = [] #list of action sequence to be returned
    path_cost = 0 #assigning uniform constant path cost of 0

    #pushing current node into consideration in fringe Stack
    fringe.push((problem.getStartState(), action_seq, path_cost))

    while fringe:
        current_node = fringe.pop() #node currently into consideration
        action_seq = current_node[1]
        
        #returning action sequence if current state is the goal state 
        if problem.isGoalState(current_node[0]):
            return action_seq

        #checking and adding current_state to list of explored/already visited nodes, if absent
        if current_node[0] not in explored_nodes:
            explored_nodes.append(current_node[0])

            for current_state in problem.getSuccessors(current_node[0]):
                next_action = list(current_node[1])
                next_action.append(current_state[1])

                fringe.push((current_state[0], next_action, current_state[2]))
    return action_seq

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    explored_nodes = [] #maintaining tuple of immutable expanded nodes
    action_seq = [] #list of action sequence to be returned
    path_cost = 0 #assigning uniform constant path cost of 0

    #pushing current node into consideration in fringe Stack
    fringe.push((problem.getStartState(), action_seq, path_cost))


    while fringe:
        current_node = fringe.pop() #node currently into consideration
        
        
        #returning action sequence if current state is the goal state 
        if problem.isGoalState(current_node[0]):
            return current_node[1]

        #checking and adding current_state to list of explored/already visited nodes, if absent
        if current_node[0] not in explored_nodes:
            explored_nodes.append(current_node[0])

            for current_state, action, cost in problem.getSuccessors(current_node[0]):
                next_action = current_node[1] + [action]
                next_cost = current_node[2] + cost

                fringe.push((current_state, next_action, next_cost))
    util.raiseNotDefined()



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    explored_nodes = [] #maintaining tuple of immutable expanded nodes
    action_seq = [] #list of action sequence to be returned
    path_cost = 0 #assigning uniform constant path cost of 0


    #pushing current node into consideration in fringe Stack
    fringe.push((problem.getStartState(), action_seq, path_cost), path_cost)

    while fringe:
    #node currently into consideration; it has current_node[0]=state, current_node[1]=action and, 
    #current_node[2]=cost; parameters    
        current_node = fringe.pop() 
        
        #returning action sequence if current state is the goal state 
        if problem.isGoalState(current_node[0]):
            return current_node[1]

        #checking and adding current_state to list of explored/already visited nodes, if absent
        if current_node[0] not in explored_nodes:
            explored_nodes.append(current_node[0])

            for current_state, action, cost in problem.getSuccessors(current_node[0]):
                next_action = current_node[1] + [action]
                next_cost = current_node[2] + cost

                fringe.push((current_state, next_action, next_cost),next_cost)
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    explored_nodes = [] #maintaining tuple of immutable expanded nodes
    action_seq = [] #list of action sequence to be returned
    path_cost = 0 #assigning uniform constant path cost of 0


    #pushing current node into consideration in fringe Stack
    fringe.push((problem.getStartState(), action_seq, path_cost), 0)

    while fringe:
    #node currently into consideration; it has current_node[0]=state, current_node[1]=action and, 
    #current_node[2]=cost; parameters    
        current_node = fringe.pop() 
        
        #returning action sequence if current state is the goal state 
        if problem.isGoalState(current_node[0]):
            return current_node[1]

        #checking and adding current_state to list of explored/already visited nodes, if absent
        if current_node[0] not in explored_nodes:
            explored_nodes.append(current_node[0])

            for current_state, action, cost in problem.getSuccessors(current_node[0]):
                next_action = current_node[1] + [action]
                next_cost = current_node[2] + cost
                h_cost = next_cost + heuristic(current_state,problem)

                fringe.push((current_state, next_action, next_cost),h_cost)
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
