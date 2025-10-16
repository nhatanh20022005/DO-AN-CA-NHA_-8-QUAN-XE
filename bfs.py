
import numpy as np
from collections import deque

class BFS:
    def __init__(self, goal_state, start_state):
        self.goal = goal_state
        self.start = start_state

    def _sinh_trang_thai(self, current, queue, row, explored, parent):
        N = current.shape[0]
        for j in range(N):
            if current[:, j].sum() == 0:  
                new_state = current.copy()
                new_state[row, j] = 1
                new_bytes = new_state.tobytes()
                if new_bytes not in explored:
                    queue.append(new_state)
                    explored.add(new_bytes)
                    parent[new_bytes] = current.tobytes()

    def run(self):
        queue = deque([self.start])
        explored = {self.start.tobytes()}
        parent = {self.start.tobytes(): None}

        while queue:
            current = queue.popleft()
            if np.array_equal(current, self.goal):
                return current, parent

            for i in range(current.shape[0]):
                if 1 not in current[i]:
                    self._sinh_trang_thai(current, queue, i, explored, parent)
                    break
        return None, parent

    def trace_path(self, parent, last):
        path = []
        dtype, shape = last.dtype, last.shape
        key = last.tobytes()
        while key is not None:
            arr = np.frombuffer(key, dtype=dtype).reshape(shape)
            path.append(arr)
            key = parent.get(key, None)
        return path[::-1]

    def generator(self):
        result, parent = self.run()
        if result is None:
            return
        path = self.trace_path(parent, result)
        for state in path:
            yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]
