import numpy as np

class AndOrSearch:
    def __init__(self, start_board, goal_board, n=8):
        self.start_board = start_board
        self.goal_board = goal_board
        self.n = n
    
    def next_row(self, board):
        """Tìm hàng đầu tiên chưa có xe"""
        for r in range(board.shape[0]):
            if 1 not in board[r]:
                return r
        return None

    def or_search(self, state, goal, visited):
        if np.array_equal(state, goal):
            return "Thành công"

        key = state.tobytes()
        if key in visited:
            return None
        visited[key] = True

        r = self.next_row(state)
        if r is None:
            return None

        for c in range(self.n):
            if state[:, c].sum() == 0:  
                new_state = state.copy()
                new_state[r, c] = 1
                plan = self.and_search(new_state, goal, visited)
                if plan is not None:
                    return ((r, c), plan)  

        return None

    def and_search(self, state, goal, visited):
        """AND node: tiếp tục tìm kế hoạch ở hàng tiếp theo"""
        return self.or_search(state, goal, visited)

    def and_or_search(self, state, goal):
        plan = self.or_search(state, goal, {})
        return plan

    def traverse(self, plan, state):
        if plan == "Thành công":
            yield state
        elif isinstance(plan, tuple) or isinstance(plan, list):
            (r, c), subplan = plan
            new_state = state.copy()
            new_state[r, c] = 1
            yield new_state
            for s in self.traverse(subplan, new_state):
                yield s

    def run(self):
        plan = self.and_or_search(self.start_board, self.goal_board)
        if plan is None:
            print("Không tìm thấy kế hoạch (AND-OR thất bại).")
            return

        for s in self.traverse(plan, self.start_board.copy()):
            yield [(r, c) for r in range(s.shape[0]) for c in range(s.shape[1]) if s[r, c] == 1]
