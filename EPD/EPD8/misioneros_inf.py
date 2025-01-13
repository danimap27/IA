from search import *

# ______________________________________________________________________________

class Misioneros(Problem):
    """ Tres misioneros y tres caníbales hacen un viaje juntos, pero el camino está cortado por un rio.
    En la orilla encuentran una lancha que los ayuda a pasar, pero sólo puede llevar dos a la vez y
    existe el peligro de que, en cualquier orilla, si los caníbales son más numerosos que los misioneros,
    estos últimos pueden servir de alimento.  """

    def getMisioneros(self, state):
        """Devuelve el número de misioneros a la izquierda del rio"""

        return state[0]

    def getCanibales(self, state):
        """Devuelve el número de canívales a la izquierda del rio"""

        return state[1]

    def getBarca(self, state):
        """Devuelve la orilla del rio en la que se encuentra la barca, 0-derecha o 1-izquierda"""

        return state[2]

    def estadoPeligroso(self, m, c):
        return ((m < c and m != 0) or (m > c and m != 3))


    def canMoveBoat(self, state, where):
        retVal = True

        if (where == 'M1C1'):
            if (self.getBarca(state) == 1):
                retVal = ((self.getMisioneros(state) >= 1) and (self.getCanibales(state) >= 1) and
                          (not self.estadoPeligroso(self.getMisioneros(state)-1, self.getCanibales(state)-1)))
            else:
                retVal = ((3-self.getMisioneros(state) >= 1) and (3-self.getCanibales(state) >= 1) and
                          (not self.estadoPeligroso(self.getMisioneros(state)+1, self.getCanibales(state)+1)))
        elif (where == 'M1C0'):
            if (self.getBarca(state) == 1):
                retVal = ((self.getMisioneros(state) >= 1) and
                          (not self.estadoPeligroso(self.getMisioneros(state)-1, self.getCanibales(state))))
            else:
                retVal = ((3-self.getMisioneros(state) >= 1) and
                          (not self.estadoPeligroso(self.getMisioneros(state)+1, self.getCanibales(state))))
        elif (where == 'M0C1'):
            if (self.getBarca(state) == 1):
                retVal = ((self.getCanibales(state) >= 1) and
                          (not self.estadoPeligroso(self.getMisioneros(state), self.getCanibales(state)-1)))
            else:
                retVal = ((3-self.getCanibales(state) >= 1) and
                          (not self.estadoPeligroso(self.getMisioneros(state), self.getCanibales(state)+1)))
        elif (where == 'M2C0'):
            if (self.getBarca(state) == 1):
                retVal = ((self.getMisioneros(state) >= 2) and
                          (not self.estadoPeligroso(self.getMisioneros(state)-2, self.getCanibales(state))))
            else:
                retVal = ((3-self.getMisioneros(state) >= 2) and
                          (not self.estadoPeligroso(self.getMisioneros(state)+2, self.getCanibales(state))))
        elif (where == 'M0C2'):
            if (self.getBarca(state) == 1):
                retVal = ((self.getCanibales(state) >= 2) and
                          (not self.estadoPeligroso(self.getMisioneros(state), self.getCanibales(state)-2)))
            else:
                retVal = ((3-self.getCanibales(state) >= 2) and
                          (not self.estadoPeligroso(self.getMisioneros(state), self.getCanibales(state)+2)))

        return retVal;

    def moveBoatM1C1(self,state):
        if (self.getBarca(state) == 1):
            state[2] = 0
            state[0] -= 1
            state[1] -= 1
        else:
            state[2] = 1
            state[0] += 1
            state[1] += 1

    def moveBoatM1C0(self,state):
        if (self.getBarca(state) == 1):
            state[2] = 0
            state[0] -= 1
        else:
            state[2] = 1
            state[0] += 1

    def moveBoatM0C1(self,state):
        if (self.getBarca(state) == 1):
            state[2] = 0
            state[1] -= 1
        else:
            state[2] = 1
            state[1] += 1

    def moveBoatM2C0(self,state):
        if (self.getBarca(state) == 1):
            state[2] = 0
            state[0] -= 2
        else:
            state[2] = 1
            state[0] += 2

    def moveBoatM0C2(self,state):
        if (self.getBarca(state) == 1):
            state[2] = 0
            state[1] -= 2
        else:
            state[2] = 1
            state[1] += 2


    def __init__(self, initial=(3, 3, 1), goal=(0, 0, 0)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = []

        if self.canMoveBoat(state,'M1C1'):
            possible_actions.append('M1C1')
        if self.canMoveBoat(state,'M1C0'):
            possible_actions.append('M1C0')
        if self.canMoveBoat(state,'M0C1'):
            possible_actions.append('M0C1')
        if self.canMoveBoat(state,'M2C0'):
            possible_actions.append('M2C0')
        if self.canMoveBoat(state,'M0C2'):
            possible_actions.append('M0C2')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = list(state)

        if (action == 'M1C1'):
            self.moveBoatM1C1(new_state)
        elif (action == 'M1C0'):
            self.moveBoatM1C0(new_state)
        elif (action == 'M0C1'):
            self.moveBoatM0C1(new_state)
        elif (action == 'M2C0'):
            self.moveBoatM2C0(new_state)
        elif (action == 'M0C2'):
            self.moveBoatM0C2(new_state)

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal


    def h(self, node):
        """ Return the heuristic value for a given state."""

        return self.getMisioneros(node.state) + self.getCanibales(node.state)

# ______________________________________________________________________________


if __name__ == '__main__':

    print('Problema de los Misioneros y los Caníbales.')

    myc = Misioneros()

    print("Resultados con breadth_first_tree_search:", breadth_first_tree_search(myc).solution())
    print("Resultados con breadth_first_graph_search:", breadth_first_graph_search(myc).solution())
    print("Resultados con depth_first_graph_search:", depth_first_graph_search(myc).solution())
#    print("REsultados con depth_first_tree_search:", depth_first_tree_search(myc).solution()) # entra en bucle
#    print("REsultados con best_first_graph_search:", best_first_graph_search(myc).solution())
    print("Resultados con uniform_cost_search:", uniform_cost_search(myc).solution())

    print("REsultados con depth_limited_search:", depth_limited_search(myc).solution())

    print("REsultados con iterative_deepening_search:", iterative_deepening_search(myc).solution())

#    print("REsultados con bidirectional_search:", bidirectional_search(myc).solution())

    print("REsultados con A*:", astar_search(myc).solution())



