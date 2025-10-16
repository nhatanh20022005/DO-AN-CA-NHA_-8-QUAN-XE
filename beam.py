
import numpy as np

def heuristic_1(board, goal):
    """Đánh giá độ khác biệt giữa board và goal"""
    return np.sum(np.abs(board - goal))

def sinh_trang_thai_beam(board, goal):
    n = board.shape[0]
    states = []
    for r in range(n):
        for c in range(n):
            if board[r, c] == 0 and goal[r, c] == 1:
                new_board = board.copy()
                new_board[r, c] = 1
                states.append(new_board)
    return states

def beam_search(start, goal, k=3):
    print(f"Bắt đầu BEAM SEARCH (k={k})")
    frontier = [(heuristic_1(start, goal), start)]
    explored = {start.tobytes(): None}
    step = 0

    while frontier:
        step += 1
        frontier.sort(key=lambda x: x[0])
        frontier = frontier[:k]
        print(f"\n--- Vòng {step}, beam size = {len(frontier)} ---")

        new_frontier = []
        for h, state in frontier:
            print(f"• Trạng thái có h = {h}")
            print(state)

            if np.array_equal(state, goal):
                print("\n✅ Đã đạt trạng thái đích!")
                return state, explored

            children = sinh_trang_thai_beam(state, goal)
            for child in children:
                b = child.tobytes()
                if b not in explored:
                    explored[b] = state.tobytes()
                    new_frontier.append((heuristic_1(child, goal), child))

        if not new_frontier:
            print("\nKhông còn trạng thái con!")
            break

        frontier = new_frontier

    print("\n Beam Search không tìm thấy lời giải!")
    return None, explored

def truy_vet(cha_map, trang_thai_cuoi):
    duong_di = []
    dtype, shape = trang_thai_cuoi.dtype, trang_thai_cuoi.shape
    node = trang_thai_cuoi.tobytes()
    while node is not None:
        mang = np.frombuffer(node, dtype=dtype).reshape(shape)
        duong_di.append(mang)
        node = cha_map.get(node, None)
    return duong_di[::-1]

def tu_dong_Beam(goal_board, start_board, k=3):
    kq, cha_map = beam_search(start_board, goal_board, k)
    if kq is None:
        print("Không tìm thấy giải pháp!")
        return

    duong_di = truy_vet(cha_map, kq)
    print(f"\nTổng số bước Beam Search: {len(duong_di)}")
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0])
                        for c in range(state.shape[1])
                        if state[r, c] == 1]

class Beam:
    def __init__(self, goal, start, k=3):
        self.goal = goal
        self.start = start
        self.k = k

    def generator(self):
        return tu_dong_Beam(self.goal, self.start, self.k)
