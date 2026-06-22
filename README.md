# Dijkstra's Pathfinding Visualiser

An interactive browser-based algorithm visualiser built with Python and Pygame.

This project was designed to strengthen my understanding of Dijkstra’s shortest-path algorithm by applying it in a practical visual environment. It also gave me experience building an interactive Python application and deploying it to the web using Pygbag, GitHub Actions and GitHub Pages.

## Live Demo

[Open the Dijkstra Pathfinding Visualiser](https://jacksonjgee.github.io/dijkstras_pathfinding_visualiser/)

![Dijkstra pathfinding visualiser showing a weighted graph and highlighted shortest path](images/image.png)

## Overview

This project allows users to create a weighted graph and calculate the shortest path between two selected nodes.

Users can:

* Create up to 26 nodes
* Connect nodes with weighted edges
* Select a start node
* Select an end node
* Run Dijkstra’s shortest-path algorithm
* View the shortest path and total distance

The calculated shortest path is highlighted visually, making it easier to understand how Dijkstra’s algorithm explores a weighted graph and determines the minimum-distance route.

## User Interaction

| Action                       | Input                        |
| ---------------------------- | ---------------------------- |
| Create a node                | Left-click on empty space    |
| Connect two nodes            | Click one node, then another |
| Select the start node        | Press `S`, then click a node |
| Select the end node          | Press `E`, then click a node |
| Calculate the shortest path  | Press `SPACE`                |
| Cancel the current selection | Press `ESC`                  |
| Reset the graph              | Press `R`                    |

## How It Works

The graph is represented using an adjacency-list data structure.

Each node stores its neighbouring nodes and the weight of each connection. When a shortest path is requested, Dijkstra’s algorithm uses a custom minimum heap priority queue to repeatedly process the node with the smallest known distance.

The algorithm produces:

* The shortest known distance to each node
* The previous node used to reach each destination
* The final shortest path from the selected start node to the selected end node

## Project Structure

```text
dijkstras_game/
├── main.py
├── src/
│   ├── __init__.py
│   ├── game.py
│   ├── graph.py
│   ├── dijkstra.py
│   └── heap_priority_queue.py
├── images/
│   └── image.png
├── requirements.txt
└── README.md
```

## File Responsibilities

* `main.py` starts the application.
* `game.py` handles rendering, input and application state.
* `graph.py` stores nodes, edges and weights.
* `dijkstra.py` contains the shortest-path algorithm.
* `heap_priority_queue.py` contains the custom minimum heap implementation.

## Technologies Used

* Python
* Pygame
* Pygbag
* GitHub Pages
* GitHub Actions

## Learning Outcomes

Through this project, I developed a stronger understanding of:

* Dijkstra’s shortest-path algorithm
* Graph data structures
* Adjacency lists
* Minimum heap priority queues
* Object-oriented Python
* Event-driven programming with Pygame
* Browser deployment using Pygbag
* Automated deployment using GitHub Actions and GitHub Pages
