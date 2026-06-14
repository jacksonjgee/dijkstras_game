import math
import random
import pygame

from src.graph import Graph
from src.dijkstra import dijkstra


class Game:
    WIDTH = 1280
    HEIGHT = 1024

    NODE_RADIUS = 25
    MAX_NODES = 26

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)
        )
        pygame.display.set_caption("Dijkstra's Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.graph = Graph()

        self.nodes = []
        self.edges = []

        self.start_node = None
        self.target_node = None
        self.selected_node = None
        self.selection_mode = None

        self.shortest_path = []
        self.shortest_distance = None

        self.message = ""

        self.node_font = pygame.font.SysFont(None, 28)
        self.weight_font = pygame.font.SysFont(None, 25)
        self.instruction_font = pygame.font.SysFont(None, 25)
        self.result_font = pygame.font.SysFont(None, 32)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event)

            elif event.type == pygame.KEYDOWN:
                self.handle_key_press(event)

    def handle_mouse_click(self, event):
        if event.button != 1:
            return

        clicked_node = self.get_clicked_node(event.pos)

        # The player clicked an existing node
        if clicked_node is not None:

            if self.selection_mode == "start":
                self.start_node = clicked_node
                self.selection_mode = None
                self.clear_shortest_path()
                self.message = f"Start node set to {clicked_node}"
                return

            if self.selection_mode == "target":
                self.target_node = clicked_node
                self.selection_mode = None
                self.clear_shortest_path()
                self.message = f"Target node set to {clicked_node}"
                return

            # Select the first node for an edge
            if self.selected_node is None:
                self.selected_node = clicked_node
                self.message = (
                    f"Selected {clicked_node}. "
                    "Click another node to connect them."
                )
                return

            # Deselect if the same node is clicked again
            if self.selected_node == clicked_node:
                self.selected_node = None
                self.message = "Node deselected."
                return

            # Prevent duplicate edges
            if self.edge_exists(
                self.selected_node,
                clicked_node
            ):
                self.selected_node = None
                self.message = "Those nodes are already connected."
                return

            # Create an edge with a random weight
            weight = random.randint(1, 10)

            self.graph.connectNode(
                self.selected_node,
                clicked_node
            )

            self.graph.weightConnection(
                self.selected_node,
                clicked_node,
                weight
            )

            self.edges.append({
                "node1": self.selected_node,
                "node2": clicked_node,
                "weight": weight
            })

            self.message = (
                f"Connected {self.selected_node} to "
                f"{clicked_node} with weight {weight}"
            )

            self.selected_node = None
            self.clear_shortest_path()
            return

        # The player clicked empty space
        if len(self.nodes) >= self.MAX_NODES:
            self.message = "Maximum of 26 nodes reached."
            return

        if not self.position_is_valid(event.pos):
            self.message = "That position is too close to another node."
            return

        node_name = chr(65 + len(self.nodes))

        self.nodes.append({
            "name": node_name,
            "position": event.pos
        })

        self.graph.createNode(node_name)

        self.clear_shortest_path()
        self.message = f"Created node {node_name}"

    def handle_key_press(self, event):
        if event.key == pygame.K_s:
            self.selection_mode = "start"
            self.selected_node = None
            self.message = "Click a node to choose the start."

        elif event.key == pygame.K_e:
            self.selection_mode = "target"
            self.selected_node = None
            self.message = "Click a node to choose the target."

        elif event.key == pygame.K_SPACE:
            self.calculate_shortest_path()

        elif event.key == pygame.K_r:
            self.reset_game()

        elif event.key == pygame.K_ESCAPE:
            self.selected_node = None
            self.selection_mode = None
            self.message = "Selection cancelled."

    def calculate_shortest_path(self):
        if self.start_node is None or self.target_node is None:
            self.message = "Choose a start and target node first."
            return

        distances, previous = dijkstra(
            self.graph,
            self.start_node,
            self.target_node
        )

        self.shortest_path = self.build_path(
            previous,
            self.start_node,
            self.target_node
        )

        if self.shortest_path:
            self.shortest_distance = distances[self.target_node]

            path_text = " -> ".join(self.shortest_path)
            self.message = f"Shortest path: {path_text}"

        else:
            self.shortest_distance = None
            self.message = "No path exists between those nodes."

    def build_path(self, previous, start, target):
        path = []
        current = target

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        if path and path[0] == start:
            return path

        return []

    def clear_shortest_path(self):
        self.shortest_path = []
        self.shortest_distance = None

    def reset_game(self):
        self.graph = Graph()

        self.nodes.clear()
        self.edges.clear()

        self.start_node = None
        self.target_node = None
        self.selected_node = None
        self.selection_mode = None

        self.clear_shortest_path()

        self.message = "Graph reset."

    def get_clicked_node(self, mouse_position):
        for node in self.nodes:
            distance = math.dist(
                mouse_position,
                node["position"]
            )

            if distance <= self.NODE_RADIUS:
                return node["name"]

        return None

    def position_is_valid(self, new_position):
        for node in self.nodes:
            distance = math.dist(
                new_position,
                node["position"]
            )

            if distance < self.NODE_RADIUS * 3:
                return False

        return True

    def edge_exists(self, node1, node2):
        for edge in self.edges:
            same_direction = (
                edge["node1"] == node1
                and edge["node2"] == node2
            )

            opposite_direction = (
                edge["node1"] == node2
                and edge["node2"] == node1
            )

            if same_direction or opposite_direction:
                return True

        return False

    def get_node_position(self, node_name):
        for node in self.nodes:
            if node["name"] == node_name:
                return node["position"]

        return None

    def edge_is_in_shortest_path(self, edge):
        for index in range(len(self.shortest_path) - 1):
            node1 = self.shortest_path[index]
            node2 = self.shortest_path[index + 1]

            same_direction = (
                edge["node1"] == node1
                and edge["node2"] == node2
            )

            opposite_direction = (
                edge["node1"] == node2
                and edge["node2"] == node1
            )

            if same_direction or opposite_direction:
                return True

        return False

    def draw(self):
        self.screen.fill("white")

        self.draw_edges()
        self.draw_nodes()
        self.draw_interface()

        pygame.display.flip()

    def draw_edges(self):
        for edge in self.edges:
            node1_position = self.get_node_position(
                edge["node1"]
            )

            node2_position = self.get_node_position(
                edge["node2"]
            )

            line_colour = "black"
            line_width = 3

            if self.edge_is_in_shortest_path(edge):
                line_colour = "green"
                line_width = 7

            pygame.draw.line(
                self.screen,
                line_colour,
                node1_position,
                node2_position,
                line_width
            )

            middle_x = (
                node1_position[0] + node2_position[0]
            ) // 2

            middle_y = (
                node1_position[1] + node2_position[1]
            ) // 2

            weight_surface = self.weight_font.render(
                str(edge["weight"]),
                True,
                "black"
            )

            weight_rectangle = weight_surface.get_rect(
                center=(middle_x, middle_y)
            )

            pygame.draw.rect(
                self.screen,
                "white",
                weight_rectangle.inflate(10, 6)
            )

            self.screen.blit(
                weight_surface,
                weight_rectangle
            )

    def draw_nodes(self):
        for node in self.nodes:
            node_name = node["name"]
            node_position = node["position"]

            colour = "grey"

            if node_name in self.shortest_path:
                colour = "green"

            if node_name == self.selected_node:
                colour = "yellow"

            if node_name == self.start_node:
                colour = "blue"

            if node_name == self.target_node:
                colour = "red"

            pygame.draw.circle(
                self.screen,
                colour,
                node_position,
                self.NODE_RADIUS
            )

            pygame.draw.circle(
                self.screen,
                "black",
                node_position,
                self.NODE_RADIUS,
                3
            )

            node_surface = self.node_font.render(
                node_name,
                True,
                "black"
            )

            node_rectangle = node_surface.get_rect(
                center=node_position
            )

            self.screen.blit(
                node_surface,
                node_rectangle
            )

    def draw_interface(self):
        self.draw_text(
            "Click empty space: create node",
            (20, 20),
            self.instruction_font
        )

        self.draw_text(
            "Click two nodes: connect them",
            (20, 48),
            self.instruction_font
        )

        self.draw_text(
            "S: choose start   E: choose target",
            (20, 76),
            self.instruction_font
        )

        self.draw_text(
            "SPACE: calculate path   R: reset   ESC: cancel",
            (20, 104),
            self.instruction_font
        )

        self.draw_text(
            f"Nodes: {len(self.nodes)}/{self.MAX_NODES}",
            (self.WIDTH - 160, 20),
            self.instruction_font
        )

        if self.message:
            self.draw_text(
                self.message,
                (20, self.HEIGHT - 80),
                self.result_font
            )

        if self.shortest_distance is not None:
            self.draw_text(
                f"Total distance: {self.shortest_distance}",
                (20, self.HEIGHT - 45),
                self.result_font,
                "green"
            )

    def draw_text(
        self,
        text,
        position,
        font,
        colour="black"
    ):
        text_surface = font.render(
            text,
            True,
            colour
        )

        self.screen.blit(
            text_surface,
            position
        )