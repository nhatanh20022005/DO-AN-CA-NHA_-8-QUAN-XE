
import numpy as np
import heapq

def tinh_cost(ma_tran, row, col, vi_tri_dich):
    cost = 1
    for r, c in vi_tri_dich:
        if r == row:
            cost += abs(col - c)
            break
    return cost


class Greedy:
    def __init__(self, goal_state, start_state, vi_tri_dich, N=8):
        self.goal = goal_state
        self.start = start_state
        self.vi_tri_dich = vi_tri_dich
        self.N = N

    def heuristic(self, board):
        used_rows = set()
        used_cols = set()
        n = board.shape[0]
        for r in range(n):
            for c in range(n):
                if board[r, c] == 1:
                    used_rows.add(r)
                    used_cols.add(c)
        return (8 - len(used_rows)) + (8 - len(used_cols))

    def run(self):
        pq = []
        counter = 0
        heapq.heappush(pq, (self.heuristic(self.start), 0, counter, self.start.copy()))
        visited = {self.start.tobytes()}
        parent = {self.start.tobytes(): None}
        best_cost = {self.start.tobytes(): 0}
        node_count = 0

        print("Bắt đầu GREEDY SEARCH")
        print(f"Trạng thái ban đầu (cost=0, h={self.heuristic(self.start)}):")
        print(self.start)
        print(f"Dest (vi_tri_dich): {self.vi_tri_dich}")

        while pq:
            h, cost, _, state = heapq.heappop(pq)
            key = state.tobytes()
            node_count += 1

            print(f"\nNode #{node_count}: cost={cost}, h={h}")
            print("Trạng thái hiện tại:")
            print(state)

            if np.array_equal(state, self.goal):
                print(f"\nTÌM THẤY ĐÍCH sau {node_count} node!")
                print(f"Tổng chi phí cuối: {cost}, h=0")
                return state, parent, best_cost, cost

            rows_empty = np.where(np.sum(state, axis=1) == 0)[0]
            if len(rows_empty) == 0:
                continue

            row = rows_empty[0]
            for col in range(state.shape[1]):
                if state[:, col].sum() != 0:
                    continue
                new_state = state.copy()
                new_state[row, col] = 1
                child_key = new_state.tobytes()
                if child_key not in visited:
                    visited.add(child_key)
                    parent[child_key] = state
                    step_cost = tinh_cost(new_state, row, col, self.vi_tri_dich)
                    new_cost = cost + step_cost
                    best_cost[child_key] = new_cost
                    new_h = self.heuristic(new_state)
                    counter += 1
                    heapq.heappush(pq, (new_h, new_cost, counter, new_state))
                    print(f"  Sinh trạng thái con: đặt xe tại ({row}, {col}), step_cost={step_cost}, cost={new_cost}, h={new_h}")

        print(f"\nKHÔNG TÌM THẤY ĐÍCH sau {node_count} node")
        return None, {}, {}, None

    def generator(self):
        result, parent, best_cost, tong_cost = self.run()
        if result is None:
            return
        duong_di = []
        state = result
        while state is not None:
            duong_di.append(state)
            state = parent.get(state.tobytes(), None)
        duong_di.reverse()
        print(f"Đường đi GREEDY: {len(duong_di)} trạng thái, Tổng chi phí: {tong_cost}")
        for state in duong_di:
            yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]
