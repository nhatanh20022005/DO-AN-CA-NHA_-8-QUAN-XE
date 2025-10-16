
import numpy as np

def heuristic(board):
    used_rows = set()
    used_cols = set()
    n = board.shape[0]

    for r in range(n):
        for c in range(n):
            if board[r, c] == 1:
                used_rows.add(r)
                used_cols.add(c)
    return (8 - len(used_rows)) + (8 - len(used_cols))


def hill_climbing(start, Ma_Tran_Dich):
    current_board = start.copy()
    current_heuristic = heuristic(current_board)
    path = [current_board.copy()]
    step = 0

    print("Bắt đầu HILL CLIMBING SEARCH")
    print(f"Trạng thái ban đầu (h={current_heuristic}):")
    print(current_board)

    while True:
        neighbors = []
        n = current_board.shape[0]
        rook_positions = [(r, c) for r in range(n) for c in range(n) if current_board[r, c] == 1]

        for r, c in rook_positions:
            for new_c in range(n):
                if new_c != c and current_board[r, new_c] == 0:
                    neighbor = current_board.copy()
                    neighbor[r, c] = 0
                    neighbor[r, new_c] = 1
                    neighbors.append(neighbor)
            for new_r in range(n):
                if new_r != r and current_board[new_r, c] == 0:
                    neighbor = current_board.copy()
                    neighbor[r, c] = 0
                    neighbor[new_r, c] = 1
                    neighbors.append(neighbor)

        best_neighbor = current_board
        best_heuristic = current_heuristic
        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < best_heuristic:
                best_heuristic = h
                best_neighbor = neighbor

        print(f"\nStep {step}: h={current_heuristic}")
        print(current_board)

        if best_heuristic >= current_heuristic:
            print("Không còn cải thiện, dừng lại.")
            break

        current_board = best_neighbor
        current_heuristic = best_heuristic
        path.append(current_board.copy())
        step += 1

        print(f"  ➕ Cải thiện: chuyển sang trạng thái có h={best_heuristic}")

        if np.array_equal(current_board, Ma_Tran_Dich):
            print(" Đạt trạng thái đích!")
            break

    print(f"\nTổng số bước: {step}")
    print(f"Heuristic cuối: {current_heuristic}")
    return path


def tu_dong_hill_climbing(Ma_Tran_Dich, start):
    path = hill_climbing(start, Ma_Tran_Dich)
    print(f"\nĐường đi HILL CLIMBING: {len(path)} trạng thái")
    for state in path:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]

class HillClimbing:
    def __init__(self, goal_matrix, start_matrix):
        self.goal = goal_matrix
        self.start = start_matrix

    def generator(self):
        return tu_dong_hill_climbing(self.goal, self.start)
