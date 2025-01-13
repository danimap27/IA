from search import *

mapa = (('O', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'O'),
        ('O', 'X', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O'),
        ('O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'O'),
        ('O', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'O'),
        ('O', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X'),
        ('O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X'),
        ('O', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X'),
        ('O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X'),
        ('O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X'),
        ('O', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'O', 'X'))

class Laberinto(Problem):
    """ Problema del laberinto donde un robot iría desde una posición de entrada a una de salida """

    def canMoveLab(self, state, where):
        retVal = True

        if (where == 'LEFT'):
            retVal = ((state[1]!=0) and (mapa[state[0]][state[1]-1]!='X'))
        elif (where == 'RIGHT'):
            retVal = ((state[1]!=9) and (mapa[state[0]][state[1]+1]!='X'))
        elif (where == 'UP'):
            retVal = ((state[0]!=0) and (mapa[state[0]-1][state[1]]!='X'))
        elif (where == 'DOWN'):
            retVal = ((state[0]!=9) and (mapa[state[0]+1][state[1]]!='X'))

        return retVal

    def __init__(self, initial=(4, 0), goal=(0, 9)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = []

        if self.canMoveLab(state,'LEFT'):
            possible_actions.append('LEFT')
        if self.canMoveLab(state,'RIGHT'):
            possible_actions.append('RIGHT')
        if self.canMoveLab(state,'UP'):
            possible_actions.append('UP')
        if self.canMoveLab(state,'DOWN'):
            possible_actions.append('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = list(state)

        if (action == 'LEFT'):
            new_state[1] -= 1
        elif (action == 'RIGHT'):
            new_state[1] += 1
        elif (action == 'UP'):
            new_state[0] -= 1
        elif (action == 'DOWN'):
            new_state[0] += 1

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def h(self, node):
        """ Return the heuristic value for a given state."""

        return abs(self.goal[0] - node.state[0]) + abs(self.goal[1] - node.state[1])

# Comienzo--------

if __name__ == '__main__':
    print('Laberinto.')

    lab = Laberinto()

    print(astar_search(lab).solution())


