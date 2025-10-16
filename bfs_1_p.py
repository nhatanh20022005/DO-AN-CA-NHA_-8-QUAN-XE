
import numpy as np
from collections import deque

class BFS1P:
    def __init__(self, co_dinh, N=8):
        self.co_dinh = co_dinh
        self.N = N

    def khong_tan_cong(self, pos, quan_co):
        r, c = pos
        for (r2, c2) in quan_co:
            if r == r2 or c == c2:
                return False
        return True

    def sinh_trang_thai(self, trang_thai):
        quan_hien_tai = trang_thai.copy()

        if len(quan_hien_tai) < self.N:
            for r in range(self.N):
                for c in range(self.N):
                    pos = (r, c)
                    if pos in quan_hien_tai or pos == self.co_dinh:
                        continue
                    if self.khong_tan_cong(pos, quan_hien_tai):
                        yield quan_hien_tai + [pos]

        for i, (r_old, c_old) in enumerate(quan_hien_tai):
            if (r_old, c_old) == self.co_dinh:
                continue
            for r in range(self.N):
                for c in range(self.N):
                    pos = (r, c)
                    if pos in quan_hien_tai:
                        continue
                    if self.khong_tan_cong(pos, [q for j, q in enumerate(quan_hien_tai) if j != i]):
                        trang_moi = quan_hien_tai.copy()
                        trang_moi[i] = pos
                        yield trang_moi

    def BFS_1_P(self):
        start = [self.co_dinh]
        frontier = deque([(start, [start])])
        visited = set()
        visited.add(tuple(start))

        while frontier:
            trang_thai, lich_su = frontier.popleft()
            if len(trang_thai) == self.N:
                return trang_thai, lich_su

            for trang_moi in self.sinh_trang_thai(trang_thai):
                trang_tuple = tuple(sorted(trang_moi))
                if trang_tuple not in visited:
                    visited.add(trang_tuple)
                    frontier.append((trang_moi, lich_su + [trang_moi]))
        return None, []

    def in_ban_co(self, state):
        board = np.zeros((self.N, self.N), dtype=int)
        for (r, c) in state:
            board[r][c] = 1
        for row in board:
            print(" ".join(str(x) for x in row))
        print("-" * 30)

    def run(self):
        goal, history = self.BFS_1_P()
        if goal is None:
            print("Không tìm thấy lời giải!")
            return

        print("BFS_1_P đã tìm thấy lời giải! Đường đi có", len(history), "bước.")
        for i, state in enumerate(history):
            print("Bước", i, ":", state)
            self.in_ban_co(state)
            yield state
