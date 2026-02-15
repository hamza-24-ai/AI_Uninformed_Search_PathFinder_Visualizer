import matplotlib.pyplot as plt
from grid import create_grid, setup_plot
from algorithm import bfs,dfs,ucs,iddfs,dls,bidirectional_search


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

def getting_user_limit():

    while True:
        user_limit = input("Enter Limit (1->20) : ")
        if user_limit.isdigit():
            user=int(user_limit)
            if 20 > user >= 1:
                break
        print("Invalid Input , Enter the Valid Input ")

    return user

def main():

    my_grid, my_cost = create_grid(20,20)
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
    elif choice == '3':
        print("Uniform Cost Search Is Working....")
        path = ucs(my_grid,my_cost,start_node,goal_node,update_gui)
    elif choice == '4':
        print("Iterative Deepining Depth First Search Is Working....")
        path = iddfs(my_grid,start_node,goal_node,50,update_gui)
    elif choice == '5':
        limit = getting_user_limit()

        print("Depth Limiting search is starting....")
        path = dls(my_grid,start_node,goal_node,limit,update_gui)
    elif choice == '6':
        print("Bidirectional_Search is Working....")
        path = bidirectional_search(my_grid,start_node,goal_node,update_gui)


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