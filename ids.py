
import numpy as np
from dls import DLS 
# 

class IDS:
    def __init__(self, goal_state, start_state, N=8):
        self.goal = goal_state
        self.start = start_state
        self.N = N
        self.dls = DLS(goal_state, start_state, limit=N)

    def IDS(self, ma_tran_dich, trang_thai_ban_dau, N=8):
        """IDS: Lặp depth limit từ 0 -> N, mỗi lần gọi lại DLS"""
        for limit in range(N + 1):
            kq, cha_map = self.dls.DLS(ma_tran_dich, trang_thai_ban_dau, limit)
            if kq is not None:
                return kq, cha_map
        return None, {} 

    def tu_dong_IDS(self, ma_tran_dich, trang_thai_ban_dau, N=8):
        kq, cha_map = self.IDS(ma_tran_dich, trang_thai_ban_dau, N)
        if kq is None:
            return
        duong_di = self.dls.truy_vet_DLS(cha_map, kq) 
        for state in duong_di:
            yield [
                (r, c)
                for r in range(state.shape[0])
                for c in range(state.shape[1])
                if state[r, c] == 1
            ]

    def generator(self):
        return self.tu_dong_IDS(self.goal, self.start, self.N)
