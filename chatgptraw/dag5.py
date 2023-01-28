class DAGVisualizer:
    def __init__(self, dag):
        self.dag = dag
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("DAG Visualizer")
        self.selected_node = None

    def handle_mouse_events(self):
        pos = pygame.mouse.get_pos()
        # Check if a node is clicked
        for node in self.dag.graph:
            if (node.x - pos[0]) ** 2 + (node.y - pos[1]) ** 2 <= 20 ** 2:
                self.selected_node = node
                break
        # Check if the user has clicked on the background
        if (self.selected_node is None and 
            pygame.mouse.get_pressed()[0]):
            self.selected_node = Node(pos[0], pos[1], value=float(input("Enter the value of the node:")))
            self.dag.add_node(self.selected_node)
        elif (self.selected_node is not None and 
              pygame.mouse.get_pressed()[2]):
            self.dag.remove_node(self.selected_node)
            self.selected_node = None

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_events()
                elif event.type == pygame.MOUSEMOTION:
                    if self.selected_node is not None:
                        self.selected_node.x, self.selected_node.y = event.pos

            self.screen.fill((255, 255, 255))

            # Draw edges
            for node1 in self.dag.graph:
                for node2 in self.dag.graph[node1]:
                    pygame.draw.line(self.screen, (0, 0, 0), 
                                     (node1.x, node1.y), 
                                     (node2.x, node2.y), 2)

            # Draw nodes
            for node in self.dag.graph:
                pygame.draw.circle(self.screen, (255, 0, 0), 
                                   (node.x, node.y), 20)
                font = pygame.font.Font(None, 30)
                text = font.render(str(node.val), 1, (0, 0, 0))
                self.screen.blit(text, (node.x - 20, node.y - 20))

            pygame.display.update()
        pygame.quit()
