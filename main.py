import matplotlib.pyplot as plt
from grid import create_grid, setup_plot
from algorithm import bfs

def main():

    my_grid = create_grid(20,20)
    start_node = (2,2)
    goal_node = (15,15)

    my_grid[start_node] = 2
    my_grid[goal_node] = 3

    fig,ax,img = setup_plot(my_grid)

    def update_gui(temp_grid):
        img.set_data(temp_grid)
        plt.pause(0.01)

    print("BFS Algorithm is starting....")
    path = bfs(my_grid,start_node,goal_node,update_gui)

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