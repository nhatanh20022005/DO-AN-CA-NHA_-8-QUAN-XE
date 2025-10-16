
import numpy as np
import heapq
def tinh_cost(state, row, col, vi_tri_dich):
    for (r, c) in vi_tri_dich:
        if r == row:
            return abs(col - c)
    return 8  

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


def A_star(start, Ma_Tran_Dich, vi_tri_dich):
    pq = []
    counter = 0
    h_start = heuristic(start)
    heapq.heappush(pq, (0 + h_start, 0, counter, start.copy()))  
    parent = {start.tobytes(): None}
    best_g = {start.tobytes(): 0}
    node_count = 0

    print("Bắt đầu A* SEARCH")
    print(f"Trạng thái ban đầu (g=0, h={h_start}, f={h_start}):")
    print(start)

    while pq:
        f, g, _, state = heapq.heappop(pq)
        key = state.tobytes()
        node_count += 1

        if best_g.get(key, float('inf')) < g:
            continue

        print(f"\nNode #{node_count}: g={g}, h={heuristic(state)}, f={f}")
        print("Trạng thái hiện tại:")
        print(state)

        if np.array_equal(state, Ma_Tran_Dich):
            print(f"\nTÌM THẤY ĐÍCH sau {node_count} node!")
            print(f"Tổng chi phí g cuối: {g}, h=0, f={f}")
            return state, parent, best_g, g

        rows_empty = np.where(np.sum(state, axis=1) == 0)[0]
        if len(rows_empty) == 0:
            print("Không còn hàng trống, bỏ qua")
            continue

        row = rows_empty[0]
        print(f"Đặt xe ở hàng {row}")
        print(f"Các cột trống: {[col for col in range(state.shape[1]) if state[:, col].sum() == 0]}")

        for col in range(state.shape[1]):
            if state[:, col].sum() != 0:
                continue
            child = state.copy()
            child[row, col] = 1
            step_cost = tinh_cost(child, row, col, vi_tri_dich)
            new_g = g + step_cost
            new_h = heuristic(child)
            new_f = new_g + new_h

            child_key = child.tobytes()
            if new_g < best_g.get(child_key, float('inf')):
                best_g[child_key] = new_g
                parent[child_key] = state
                counter += 1
                heapq.heappush(pq, (new_f, new_g, counter, child))
                print(f"  Sinh trạng thái con: đặt xe tại ({row}, {col}), step_cost={step_cost}, g={new_g}, h={new_h}, f={new_f}")

    print(f"\nKHÔNG TÌM THẤY ĐÍCH sau {node_count} node")
    return None, parent, best_g, None


def truy_vet_A_star(parent, trang_thai_cuoi):
    if trang_thai_cuoi is None:
        return []

    duong_di = []
    dtype, shape = trang_thai_cuoi.dtype, trang_thai_cuoi.shape
    key = trang_thai_cuoi.tobytes()
    while key is not None:
        mang_1c = np.frombuffer(key, dtype=dtype)
        mang_2c = mang_1c.reshape(shape).copy()
        duong_di.append(mang_2c)
        cha = parent.get(key, None)
        key = cha.tobytes() if cha is not None else None
    return duong_di[::-1]


def tu_dong_A_star(Ma_Tran_Dich, start, vi_tri_dich):
    kq, parent, _, g = A_star(start, Ma_Tran_Dich, vi_tri_dich)
    if kq is None:
        return
    duong_di = truy_vet_A_star(parent, kq)
    print(f"Đường đi A*: {len(duong_di)} trạng thái")
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]


class AStar:
    def __init__(self, goal_matrix, start_matrix, goal_pos):
        self.goal = goal_matrix
        self.start = start_matrix
        self.goal_pos = goal_pos

    def generator(self):
        return tu_dong_A_star(self.goal, self.start, self.goal_pos)
