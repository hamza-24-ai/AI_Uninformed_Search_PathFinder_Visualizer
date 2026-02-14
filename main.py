import matplotlib.pyplot as plt
from grid import create_grid, setup_plot
from algorithm import bfs,dfs


def getvalues():
    while True:
        start_input = input("Start Node (0-19): ")

        if start_input.isdigit():
            start = int(start_input)

            if 0 <= start < 20:
                break
        print("Invalid! Please enter a number between 0 and 19.")

    while True:
        goal_input = input("Goal Node (0-19): ")
        if goal_input.isdigit():
            goal = int(goal_input)
            if 0 <= goal < 20:
                break
        print("Invalid! Please enter a number between 0 and 19.")

    return start, goal
def main():

    my_grid = create_grid(20,20)
    s,g = getvalues()
    start_node = (s,s)
    goal_node = (g,g)

    my_grid[start_node] = 2
    my_grid[goal_node] = 3

    fig,ax,img = setup_plot(my_grid)

    def update_gui(temp_grid):
        img.set_data(temp_grid)
        plt.pause(0.01)

    path=0
    while True:
        choice = input(''' Please Enter your Choice 
                              1. BFS Algorithm 
                              2. DFS Algorithm 
                              3. UCS Algorithm 
                              4. IDDFS Algorithm
                              5. DLS Algorithm 
                              6. BS Algorithm  : ''')
        if '1' <= choice <= '6':
            break
        print('Please Enter Value in given Range ')
    if choice == '1':
        print("BFS Algorithm is starting....")
        path = bfs(my_grid, start_node, goal_node, update_gui)
    elif choice == '2':
        print("DFS is Running....")
        path = dfs(my_grid, start_node, goal_node, update_gui)

    if path:
        print("Path Find !!")
        for r,c in path:
            if (r, c) != goal_node:

                my_grid[r][c]=5
        update_gui(my_grid)
    else:
        print("Path is not find")

    plt.show()

if __name__ == "__main__":
    main()