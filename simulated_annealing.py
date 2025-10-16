import numpy as np
import random
import math

class SimulatedAnnealing:
    def __init__(self, start_board, goal_board, T=1000.0, cooling_rate=0.995, max_iter=10000):
        self.start_board = start_board
        self.goal_board = goal_board
        self.T = T  # Initial temperature
        self.cooling_rate = cooling_rate
        self.max_iter = max_iter

    # Tính chi phí (cost) giữa trạng thái hiện tại và mục tiêu
    def tinh_cost_1(self, board, goal):
        return int(np.sum(np.abs(board - goal)))

    # Hàm khởi tạo start từ goal
    def tao_start_tu_goal(self):
        n = self.goal_board.shape[0]
        need = int(self.goal_board.sum())
        start = np.zeros_like(self.goal_board)
        cells = [(r, c) for r in range(n) for c in range(n)]
        random.shuffle(cells)
        for i in range(need):
            r, c = cells[i]
            start[r, c] = 1
        return start

    # Tìm hàng xóm ngẫu nhiên
    def neighbor_any(self, board):
        n = board.shape[0]
        new_board = board.copy()
        rook_positions = [(r,c) for r in range(n) for c in range(n) if board[r,c]==1]
        empty_positions = [(r,c) for r in range(n) for c in range(n) if board[r,c]==0]
        
        if not rook_positions or not empty_positions:
            return new_board

        r0, c0 = random.choice(rook_positions)
        r1, c1 = random.choice(empty_positions)
        new_board[r0, c0] = 0
        new_board[r1, c1] = 1
        return new_board

    # Thuật toán Simulated Annealing chính
    def simulated_annealing(self):
        # Khởi tạo trạng thái ban đầu nếu không hợp lệ
        if self.start_board.sum() != self.goal_board.sum() or self.start_board.sum() == 0:
            self.start_board = self.tao_start_tu_goal()

        current = self.start_board.copy()
        current_cost = self.tinh_cost_1(current, self.goal_board)
        history = [current.copy()]

        print("SA start cost:", current_cost)

        for step in range(self.max_iter):
            if np.array_equal(current, self.goal_board) or current_cost == 0:
                print(f"Reached goal at step {step}, cost={current_cost}")
                break

            new_state = self.neighbor_any(current)
            new_cost = self.tinh_cost_1(new_state, self.goal_board)
            delta = new_cost - current_cost

            # debug occasional
            if step % 200 == 0:
                print(f"step {step}: cost {current_cost} -> {new_cost}, T={self.T:.4f}")

            # Tiến hành cập nhật nếu cải thiện hoặc chấp nhận theo tỉ lệ
            if delta < 0 or random.random() < math.exp(-delta / self.T if self.T > 0 else 0):
                current, current_cost = new_state, new_cost
                history.append(current.copy())

            # Làm mát dần theo cooling_rate
            self.T *= self.cooling_rate
            if self.T < 1e-8:
                break

        return current, history

    # Hàm để hiển thị (generator)
    def tu_dong_SA(self):
        current, history = self.simulated_annealing()
        print("Cost cuối cùng:", self.tinh_cost_1(current, self.goal_board), "History len:", len(history))
        for state in history:
            yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]
