# EPD7: Machine Learning - Search tools
import time
#import countcalls

from search import *

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def linear(node):
    return sum([1 if node.state[i] != goal[i] else 0 for i in range(8)])


def manhattan(node):
    state = node.state
    index_goal = {0: [2, 2], 1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1]}
    index_state = {}
    index = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    x, y = 0, 0

    for i in range(len(state)):
        index_state[state[i]] = index[i]

    mhd = 0

    for i in range(8):
        for j in range(2):
            mhd = abs(index_goal[i][j] - index_state[i][j]) + mhd

    return mhd


if __name__ == '__main__':
    print('EightPuzzle.')

    puzzle = EightPuzzle((2, 4, 3, 1, 5, 6, 7, 8, 0))
    print(astar_search(puzzle).solution())
    print(astar_search(puzzle, linear).solution())

    puzzle_1 = EightPuzzle((2, 4, 3, 1, 5, 6, 7, 8, 0))
    puzzle_2 = EightPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))
    puzzle_3 = EightPuzzle((1, 2, 3, 4, 5, 7, 8, 6, 0))

    star_time = time.time()
    astar_search(puzzle_1)
    astar_search(puzzle_2)
    astar_search(puzzle_3)
    print("Tiempo transcurrido (astar-linear): ", time.time() - star_time)

    star_time = time.time()
    breadth_first_tree_search(puzzle_1)
    breadth_first_tree_search(puzzle_2)
    breadth_first_tree_search(puzzle_3)
    print("Tiempo transcurrido (astar-manhattan): ", time.time() - star_time)



'''
    star_time = time.time()
    astar_search(puzzle_1, manhattan)
    astar_search(puzzle_2, manhattan)
    astar_search(puzzle_3, manhattan)
    print("Tiempo transcurrido (astar-manhattan): ", time.time() - star_time)

    star_time = time.time()
    recursive_best_first_search(puzzle_1, linear)
    recursive_best_first_search(puzzle_2, linear)
    recursive_best_first_search(puzzle_3, linear)
    print("Tiempo transcurrido (best_first-linear): ", time.time() - star_time)

    star_time = time.time()
    recursive_best_first_search(puzzle_1, manhattan)
    recursive_best_first_search(puzzle_2, manhattan)
    recursive_best_first_search(puzzle_3, manhattan)
    print("Tiempo transcurrido (best_first-manhattan): ", time.time() - star_time)
'''
    #report([uniform_cost_search], [puzzle_1, puzzle_2, puzzle_3])
    #report((uniform_cost_search, astar_search),
    #                  (puzzle_1, puzzle_2, puzzle_3))
