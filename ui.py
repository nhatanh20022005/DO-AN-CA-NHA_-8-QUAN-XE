
import pygame, sys, random, numpy as np
from bfs import BFS
from dfs import DFS
from ucs import UCS
from dls import DLS
from ids import IDS
from greedy import Greedy
from a_star import AStar
from hill_climbing import HillClimbing
from genetic import Genetic
from beam import Beam
from simulated_annealing import SimulatedAnnealing
from and_or_search import AndOrSearch
from bfs_non import BFSNon
from bfs_1_p import BFS1P
from bk import BK
from fw import FW



from board import Board
from button import Button

class UI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Game 8 Xe - OOP Version")
        self.bg = pygame.transform.scale(pygame.image.load("bg2.png"), (1200, 700))
        self.font = pygame.font.SysFont(None, 40)
        self.clock = pygame.time.Clock()
        self.state = "menu"
        self.current_algo = None
        self.positions = None
        self.generator = None
        self.update_positions = []
        self.step_delay = 1500
        self.last_step = pygame.time.get_ticks()
        self.board = Board(self.screen)
        self.create_buttons()

    def create_buttons(self):
        self.buttons = [
            Button("BFS", 200, 60, 300, 50, (255, 253, 181), (150, 150, 150), self.font),
            Button("DFS", 200, 120, 300, 50, (255, 253, 181), (150, 150, 150), self.font),
            Button("UCS",200,180,300,50,(255,253,181),(150,150,150),self.font),
            Button("DLS",200,240,300,50,(255,253,181),(150,150,150),self.font),
            Button("IDS",200,300,300,50,(255,253,181),(150,150,150),self.font),
            Button("GREEDY",200,360,300,50,(255,253,181),(150,150,150),self.font),
            Button("A*",200,420,300,50,(255,253,181),(150,150,150),self.font),
            Button("HILL CLIMBING", 200, 480, 300, 50, (255, 253, 181), (150, 150, 150), self.font),
            Button("GENETIC", 200, 540, 300, 50, (255, 253, 181), (150, 150, 150), self.font),
            Button("BEAM", 200, 600, 300, 50, (255, 253, 181), (150, 150, 150), self.font),
            Button("SIMULATED ANNEALING", 550, 60, 350, 50, (255, 253, 181), (150,150,150), self.font),
            Button("AND-OR", 550, 120, 300, 50, (255,253,181), (150,150,150), self.font),
            Button("BFS_non", 550, 180, 300, 50, (255,253,181), (150,150,150), self.font),
            Button("BFS_par", 550, 240, 300, 50, (255,253,181), (150,150,150), self.font),
            Button("CSP BACKTRACKING", 550, 300, 300, 50, (255,253,181), (150,150,150), self.font),
            Button("FORWARD CHECKING", 550, 360, 300, 50, (255,253,181), (150,150,150), self.font)
        ]

    def random_vi_tri(self, n=8):
        cols = list(range(n))
        result = []
        for row in range(n):
            col = random.choice(cols)
            result.append((row, col))
            cols.remove(col)
        return result

    def khoi_bfs(self):
        self.current_algo = "BFS"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1
        start_matrix = np.zeros((8, 8), int)
        bfs = BFS(goal_matrix, start_matrix)
        self.generator = bfs.generator()
        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_dfs(self):
        self.current_algo = "DFS"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1

        start_matrix = np.zeros((8, 8), int)
        dfs = DFS(goal_matrix, start_matrix)
        self.generator = dfs.generator()

        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_ucs(self):
        self.current_algo = "UCS"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1

        start_matrix = np.zeros((8, 8), int)
        ucs = UCS(goal_matrix, start_matrix, goal_pos)
        self.generator = ucs.generator()

        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_dls(self):
        self.current_algo = "DLS"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1

        start_matrix = np.zeros((8, 8), int)
        dls = DLS(goal_matrix, start_matrix, limit=8)
        self.generator = dls.generator()

        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_ids(self):
        self.current_algo = "IDS"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1

        start_matrix = np.zeros((8, 8), int)
        ids = IDS(goal_matrix, start_matrix, N=8)
        self.generator = ids.generator()

        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_greedy(self):
        self.current_algo = "GREEDY"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1

        start_matrix = np.zeros((8, 8), int)
        greedy = Greedy(goal_matrix, start_matrix, goal_pos, N=8)
        self.generator = greedy.generator()

        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_a_star(self):
        self.current_algo = "A*"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1

        start_matrix = np.zeros((8, 8), int)
        a_star = AStar(goal_matrix, start_matrix, goal_pos)
        self.generator = a_star.generator()

        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_hill_climbing(self):
        self.current_algo = "Hill Climbing"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1

        start_matrix = np.zeros((8, 8), int)
        hill = HillClimbing(goal_matrix, start_matrix)
        self.generator = hill.generator()
        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_genetic(self):
        self.current_algo = "Genetic"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1

        genetic = Genetic(goal_matrix)
        self.generator = genetic.generator()
        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_beam(self):
        self.current_algo = "Beam"
        start, goal = self.random_start_goal()
        beam = Beam(goal, start, k=3)  # có thể thay k nếu muốn
        self.generator = beam.generator()
        self.update_positions = []
        self.positions = [(r, c) for r in range(start.shape[0]) for c in range(start.shape[1]) if start[r, c] == 1]
        self.state = "game"
    def khoi_SA(self):
        self.current_algo = "SA"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1
        start_matrix = np.zeros((8, 8), int)
        
        # Khởi tạo đối tượng Simulated Annealing
        sa = SimulatedAnnealing(start_matrix, goal_matrix)
        self.generator = sa.tu_dong_SA()  # Sử dụng generator từ SimulatedAnnealing
        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_ANDOR(self):
        self.current_algo = "AND-OR"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1
        start_matrix = np.zeros((8, 8), int)
        
        # Khởi tạo đối tượng AndOrSearch
        andor_search = AndOrSearch(start_matrix, goal_matrix)
        self.generator = andor_search.run()  # Sử dụng generator từ AndOrSearch
        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_BFS_non(self):
        self.current_algo = "BFS_non"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1
        start_matrix = np.zeros((8, 8), int)
        # Khởi tạo đối tượng BFSNon
        bfs_non = BFSNon(goal_matrix, start_matrix, heuristic=lambda board: np.sum(board != goal_matrix))
        self.generator = bfs_non.run()  # Sử dụng generator từ BFSNon
        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_BFS_1_P(self):
        self.current_algo = "BFS_1_P"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1
        start_matrix = np.zeros((8, 8), int)
        
        # Khởi tạo đối tượng BFS_1_P
        bfs_algo = BFS1P(goal_pos)
        self.generator = bfs_algo.run()  # Sử dụng generator từ BFS1P
        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_BK(self):
        self.current_algo = "CSP"
        goal_pos = self.random_vi_tri()
        goal_matrix = np.zeros((8, 8), int)
        for (r, c) in goal_pos:
            goal_matrix[r][c] = 1
        start_matrix = np.zeros((8, 8), int)
        
        # Khởi tạo đối tượng CSP
        csp_algo = BK(N=8)
        self.generator = csp_algo.tu_dong_CSP()  # Sử dụng generator từ CSP
        self.update_positions = []
        self.positions = goal_pos
        self.state = "game"
    def khoi_FW(self):
        self.current_algo = "CSP_Forward_Checking"
        
        # Khởi tạo đối tượng CSP
        csp_algo = FW()
        self.generator = csp_algo.generator()  # Sử dụng generator từ CSP
        
        # Reset các trạng thái vẽ
        self.update_positions = []
        self.positions = []  # Chưa có quân hậu nào lúc bắt đầu
        self.state = "game"












    def loop(self):
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.state == "menu":
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        if self.buttons[0].rect.collidepoint(mouse):
                            self.khoi_bfs()
                        elif self.buttons[1].rect.collidepoint(mouse):
                            self.khoi_dfs()
                        elif self.buttons[2].rect.collidepoint(mouse):  
                            self.khoi_ucs()
                        elif self.buttons[3].rect.collidepoint(mouse):  
                            self.khoi_dls()
                        elif self.buttons[4].rect.collidepoint(mouse):  
                            self.khoi_ids()
                        elif self.buttons[5].rect.collidepoint(mouse):  
                            self.khoi_greedy()
                        elif self.buttons[6].rect.collidepoint(mouse):  
                            self.khoi_a_star()
                        elif self.buttons[7].rect.collidepoint(mouse):  
                            self.khoi_hill_climbing()
                        elif self.buttons[8].rect.collidepoint(mouse):  
                            self.khoi_genetic()
                        elif self.buttons[9].rect.collidepoint(mouse):  
                            self.khoi_beam()
                        elif self.buttons[10].rect.collidepoint(mouse):  
                            self.khoi_SA()
                        elif self.buttons[11].rect.collidepoint(mouse):  
                            self.khoi_ANDOR()
                        elif self.buttons[12].rect.collidepoint(mouse):  
                            self.khoi_BFS_non()
                        elif self.buttons[13].rect.collidepoint(mouse):  
                            self.khoi_BFS_1_P()
                        elif self.buttons[14].rect.collidepoint(mouse):  
                            self.khoi_BK()
                        elif self.buttons[15].rect.collidepoint(mouse):  
                            self.khoi_FW()








            self.screen.blit(self.bg, (0, 0))

            if self.state == "menu":
                for btn in self.buttons:
                    btn.draw(self.screen, mouse)

            elif self.state == "game":
                now = pygame.time.get_ticks()
                if now - self.last_step > self.step_delay:
                    try:
                        self.update_positions = next(self.generator)
                    except StopIteration:
                        pass
                    self.last_step = now

                x_board = (1200 - (8 * 40 * 2 + 150)) // 2
                y_board = (700 - 8 * 40) // 2
                self.board.draw(x_board, y_board, self.update_positions)
                self.board.draw(x_board + 8 * 40 + 150, y_board, self.positions)

            pygame.display.update()
            self.clock.tick(30)
