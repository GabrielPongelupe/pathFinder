# 🤖 PathFinder – Solving the 2D Maze with the A Algorithm*
This project was developed as part of the coursework for the subject Foundations of Algorithm Design and Analysis (FPAA), taught by professor João Paulo Carneiro Aramuni, in the Software Engineering program at PUC Minas.

## 👥 Team Members
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/GabrielPongelupe">
        <img src="https://avatars.githubusercontent.com/u/130582324?v=4" width="100px;" height="100px;" style="border-radius:50%;" alt="Gabriel Pongelupe"/><br />
        <sub><b>Gabriel Pongelupe</b></sub>
      </a>
    </td>
  </tr>
  
</table>

---

## 🧭 Overview
PathFinder is a project designed to simulate a rescue robot navigating through a two-dimensional maze. The main goal is to help this robot reach a target location as quickly and efficiently as possible, while avoiding walls and obstacles that block its path. To accomplish this, we implemented the A* (A-Star) search algorithm, which is widely used in robotics, game development, and artificial intelligence for solving pathfinding problems.

A* is a heuristic-based algorithm that blends two powerful strategies: Dijkstra’s algorithm, which ensures the shortest path is found, and Greedy Best-First Search, which uses a heuristic to guide the search towards the goal. This combination allows A* to perform efficient searches even in complex environments.

## 📝 Project Summary
This project implements A* to solve the challenge of finding the optimal path between two points within a 2D grid-based maze. The maze includes:
- Free spaces (0) where the robot can move
- Obstacles (1) which the robot must avoid
- A Start point (S) and an End point (E) that define the pathfinding goal

## ❓ Problem Description
The challenge of navigating from a starting point to a destination in a grid full of obstacles is a classic problem in computer science. In this simulation, the robot must determine the shortest valid route using only adjacent movements (up, down, left, right) without stepping into walls or exiting the maze boundaries. Each step has a uniform cost, and the goal is to reach the destination using the fewest moves possible.

## 🧱 Maze Navigation Rules
- The maze is a two-dimensional matrix.
- Values represent:
  - 0 = free path
  - 1 = wall/obstacle
  - S = start point
  - E = end point
- The robot can move in four directions: up, down, left, and right.
- The movement cost is fixed at 1 for each step.

## 🧠 A* Algorithm Details
A* works by evaluating each possible move based on the formula:
f(n) = g(n) + h(n)
Where:
- g(n) is the cost to reach node n from the start
- h(n) is the heuristic estimate from node n to the goal

We used the __Manhattan distance__ as the heuristic, calculated by:
__h(n) = |x₁ - x₂| + |y₁ - y₂|__

This heuristic is suitable for grid-based movement without diagonals.

---

## ⚙️ How to Run
### Requirements
- Python 3.6 or higher
- -
### Execution
1. Clone Repository
2. Execute script:
```bash
python solution.py
```


## ⚙️ Features Implemented

### ✅ Input Handling
- Receives the maze as a 2D matrix input
- Checks and confirms the presence of:
  - 🟢 Start point (`S`)
  - 🔴 End point (`E`)
- Prevents execution if either point is missing


### ✅ Heuristic Function
- Uses Manhattan distance to guide the search efficiently

### ✅ A Algorithm*
- Explores the maze intelligently to find the shortest route
- Stops and returns “No solution” if no valid path exists

### ✅ Output
- Displays the path as a list of coordinate steps
- Optionally, renders the maze with the path visually marked

---

## 🧪 Example
__Input Maze:__
```mathematica
S 0 1 0 0  
0 0 1 0 1  
1 0 1 0 0  
1 0 0 E 1  
```

__Path Output:__
```csharp
[s(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), e(3, 3)]
```

__Maze with Path Marked:__
```mathematica
S * 1 0 0  
0 * 1 0 1  
1 * 1 0 0  
1 * * E 1  
```
## 🧪 Example 2 – No Possible Path
In this scenario, the maze configuration prevents the robot from reaching the end point due to complete blockage by obstacles.

__🔢 Input Maze:__
```text
S 0 1 0 0  
0 0 1 0 1  
1 1 1 0 0  
1 0 0 E 1
```
- S = Start point
- E = End point
- 1 = Obstacles (walls)
- 0 = Free space

### 🧠 Why No Path Exists?
- The robot starts at position (0, 0)
- The direct route toward the end at (3, 3) is completely blocked by walls in the middle row: the third row ([1, 1, 1, 0, 0]) forms an impassable barrier.
- Even alternate routes (like from the bottom left or far right) are closed off.

__🧾 Output:__
```pgsql
No path found.
```

__🔍 Visualization:__
```mathematica
S 0 1 0 0
0 0 1 0 1
1 1 1 0 0
1 0 0 E 1
```
✅ This test case demonstrates the algorithm’s ability to detect and correctly report the absence of a viable path between S and E.

---
## 📁 Code Structure
- ```calcular_heuristica(ponto1, ponto2)``` Calculates the Manhattan distance between two points. This serves as the heuristic function h(n) used in the A* algorithm.
- ```busca_a_estrela(mapa, origem, destino)``` Core implementation of the A* search algorithm.
  - Uses a priority queue (```heapq```) to explore nodes with the lowest estimated total cost ```f(n) = g(n) + h(n)```.
  - Maintains the actual cost to reach each cell (```g(n)```) and reconstructs the path once the goal is reached.
  - Returns a list of coordinates representing the optimal path, or ```None``` if no path is found.
- ```exibir_mapa_com_rota(mapa, rota)``` Generates a visual representation of the maze with the found path overlaid:
  - ```'S'```: start point
  - ```'E'```: end point
  - ```'*'```: cells in the path
  - ```'1'```: walls
  - ```'0'```: free cells
- ```main``` block
  - Initializes a sample maze with 'S' and 'E' markers.
  - Locates the start and end positions in the maze and converts them to 0 for pathfinding purposes.
  - Calls the A* search and prints either the path found or a message indicating that no solution exists.
  - Displays the maze with the marked path if a solution is found.



## 💡 Future Improvements (Optional Features)
These features were not implemented in this version, but could be added to enhance the project:
- Allow diagonal movement with a cost of √2
- Add a real-time graphical interface to visualize the robot's exploration
- Support different terrain costs (e.g., mud, sand, grass)
