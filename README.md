#Pathfinding Visualizer (Python & Matplotlib)
A real-time grid-based pathfinding visualizer built with Python. This project implements various Artificial Intelligence 
search algorithms to find the most efficient path between a Start and Goal node on a 20x20 grid.

🚀## Features
Real-time Visualization: Watch how each algorithm explores the grid.

6-Directional Movement: Supports Up, Down, Left, Right, and two Diagonals.

Obstacles: Includes a central wall to test pathfinding around barriers.

Interactive Input: Choose your own Start and Goal coordinates.

##🧠 Algorithms Implemented
Algorithm        Type        Shortest Path?        Special Feature
BFS         Breadth-First          Yes          Explores layer by layer.
DFS         Depth-First            No           Fast, but can take very long paths.
UCS         Uniform Cost           Yes          Uses Random Costs (1-100) for each cell.
DLS         Depth Limited          No           Stops at a user-defined depth limit.
IDDFS       Iterative Deepening    Yes          Combines DFS memory efficiency with BFS optimality.
Bi          Two-way BFS            Yes          Searches from both ends to meet in the middle.
directional

##🛠️ Technologies Used
Python 3.x

Matplotlib: Used for the graphical interface and real-time grid updates.

NumPy: Handles the 2D array (Grid) and cost matrix operations.

Heapq: Used for the Priority Queue in Uniform Cost Search (UCS).

##📸 Visualization Legend
🟩 Green: Start Node

🟥 Red: Goal Node

⬛ Black: Obstacle (Wall)

🟦 Blue: Exploration Area (Nodes visited by the algorithm)

🟧 Orange: Final Path found from Start to Goal

##Goal

###🏃 How to Run
Clone the repository:

##Bash
git clone https://github.com/hamza-24-ai/AI_Uninformed_Search_PathFinder_Visualizer.git

##Install dependencies:
###Bash
pip install matplotlib numpy

##Run the application:
###Bash
python main.py
