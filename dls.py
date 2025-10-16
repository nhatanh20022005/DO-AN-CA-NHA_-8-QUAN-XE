
import numpy as np

class DLS:
    def __init__(self, goal_state, start_state, limit=8):
        self.goal = goal_state
        self.start = start_state
        self.limit = limit

    def sinh_trang_thai_dls(self, ma_tran_dang_xet, hang, explored, ma_tran_cha, limit, depth):
        N = ma_tran_dang_xet.shape[0]
        trang_thai_moi = []
        if depth <= limit: 
            for j in range(N):
                if ma_tran_dang_xet[:, j].sum() == 0:  
                    con = ma_tran_dang_xet.copy()
                    con[hang, j] = 1
                    con_bytes = con.tobytes()
                    if con_bytes not in explored:
                        explored.add(con_bytes)
                        ma_tran_cha[con_bytes] = ma_tran_dang_xet.tobytes()
                        trang_thai_moi.append(con)
        return trang_thai_moi

    def DLS(self, ma_tran_dich, trang_thai_ban_dau, limit):
        stack = [(trang_thai_ban_dau, 0)] 
        explored = {trang_thai_ban_dau.tobytes()}
        ma_tran_cha = {trang_thai_ban_dau.tobytes(): None}

        while stack:
            ma_tran_dang_xet, depth = stack.pop()

            if np.array_equal(ma_tran_dang_xet, ma_tran_dich):
                return ma_tran_dang_xet, ma_tran_cha

            for i in range(ma_tran_dang_xet.shape[0]):
                if 1 not in ma_tran_dang_xet[i]:
                    children = self.sinh_trang_thai_dls(
                        ma_tran_dang_xet, i, explored, ma_tran_cha, limit, depth + 1
                    )
                    for child in reversed(children): 
                        stack.append((child, depth + 1))
                    break
        return None, ma_tran_cha

    def truy_vet_DLS(self, ma_tran_cha, trang_thai_cuoi):
        duong_di = []
        dtype, shape = trang_thai_cuoi.dtype, trang_thai_cuoi.shape
        na = trang_thai_cuoi.tobytes()
        while na is not None:
            mang_1c = np.frombuffer(na, dtype=dtype)
            mang_2c = mang_1c.reshape(shape)
            duong_di.append(mang_2c)
            na = ma_tran_cha.get(na, None)
        return duong_di[::-1]

    def tu_dong_DLS(self, ma_tran_dich, trang_thai_ban_dau, limit=8):
        kq, cha_map = self.DLS(ma_tran_dich, trang_thai_ban_dau, limit)
        if kq is None:
            return
        duong_di = self.truy_vet_DLS(cha_map, kq)
        for state in duong_di:
            yield [
                (r, c)
                for r in range(state.shape[0])
                for c in range(state.shape[1])
                if state[r, c] == 1
            ]

    def generator(self):
        return self.tu_dong_DLS(self.goal, self.start, self.limit)
