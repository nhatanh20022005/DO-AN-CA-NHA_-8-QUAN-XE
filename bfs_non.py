
import numpy as np
import heapq

class BFSNon:
    def __init__(self, ma_tran_dich, trang_thai_ban_dau, heuristic, max_depth=20):
        self.ma_tran_dich = ma_tran_dich
        self.trang_thai_ban_dau = trang_thai_ban_dau
        self.heuristic = heuristic
        self.max_depth = max_depth

    def sinh_trang_thai_hang(self, board):
        cac_trang_thai = []
        n = board.shape[0]
        for r in range(n):
            for c in range(n):
                if board[r, c] == 1: 
                    for nc in range(n):
                        if nc != c and board[r, nc] == 0:  
                            moi = np.copy(board)
                            moi[r, c], moi[r, nc] = 0, 1
                            cac_trang_thai.append(moi)
        return cac_trang_thai

    def bfs_non(self):
        pq = []  
        counter = 0
        heapq.heappush(pq, (self.heuristic(self.trang_thai_ban_dau), counter, self.trang_thai_ban_dau, []))
        counter += 1
        visited = set()

        while pq:
            _, _, board, path = heapq.heappop(pq)

            if np.array_equal(board, self.ma_tran_dich):
                return path + [board]

            key = board.tobytes()
            if key in visited:
                continue
            visited.add(key)

            if len(path) >= self.max_depth:
                continue

            for next_board in self.sinh_trang_thai_hang(board):
                next_key = next_board.tobytes()
                if next_key not in visited:
                    h = self.heuristic(next_board)
                    heapq.heappush(pq, (h, counter, next_board, path + [board]))
                    counter += 1

        return None

    def run(self):
        return self.bfs_non()
