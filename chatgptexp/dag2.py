import pygame

class DAGVisualizer:
    def __init__(self, dag):
        self.dag = dag
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("DAG Visualizer")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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

