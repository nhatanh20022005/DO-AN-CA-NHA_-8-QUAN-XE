
import numpy as np
import heapq

class UCS:
    def __init__(self, goal_state, start_state, vi_tri_dich):
        self.goal = goal_state
        self.start = start_state
        self.vi_tri_dich = vi_tri_dich

    def tinh_cost(self, ma_tran, row, col):
        cost = 1
        for r, c in self.vi_tri_dich:
            if r == row:
                cost += abs(col - c)
                break
        return cost

    def run(self):
        pq = []
        counter = 0
        heapq.heappush(pq, (0, counter, self.start.copy()))
        parent = {self.start.tobytes(): None}
        best_cost = {self.start.tobytes(): 0}
        node_count = 0

        while pq:
            cost, _, state = heapq.heappop(pq)
            key = state.tobytes()
            node_count += 1

            if best_cost.get(key, float('inf')) != cost:
                continue

            if np.array_equal(state, self.goal):
                return state, parent, best_cost, cost

            rows_empty = np.where(np.sum(state, axis=1) == 0)[0]
            if len(rows_empty) == 0:
                continue
            row = rows_empty[0]

            for col in range(state.shape[1]):
                if state[:, col].sum() != 0:
                    continue

                child = state.copy()
                child[row, col] = 1
                step_cost = self.tinh_cost(child, row, col)
                new_cost = cost + step_cost

                child_key = child.tobytes()
                if new_cost < best_cost.get(child_key, float('inf')):
                    best_cost[child_key] = new_cost
                    parent[child_key] = state
                    counter += 1
                    heapq.heappush(pq, (new_cost, counter, child))

        return None, parent, best_cost, None

    def truy_vet_UCS(self, parent, trang_thai_cuoi):
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

    def generator(self):
        result, parent, best_cost, total = self.run()
        if result is None:
            return
        path = self.truy_vet_UCS(parent, result)
        for state in path:
            yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]
