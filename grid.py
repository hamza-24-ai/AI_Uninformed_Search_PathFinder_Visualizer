import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def create_grid(rows=20, cols=20):
    grid = np.zeros((rows, cols))

    grid[5:15, 10] = 1
    costs = np.random.randint(1,101,size=(rows,cols))
    return grid,costs


def setup_plot(grid):
    # Colors: 0:White, 1:Black, 2:Green(S), 3:Red(T), 4:Blue(Explored), 5:Orange(Path)
    cmap = colors.ListedColormap(['white', 'black', 'green', 'red', '#1f77b4', '#ff7f0e'])
    bounds = [0, 1, 2, 3, 4, 5, 6]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots(figsize=(8, 8))

    img = ax.imshow(grid, cmap=cmap, norm=norm, interpolation='nearest')

    ax.set_xticks(np.arange(-.5, grid.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-.5, grid.shape[0], 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)

    return fig, ax, img