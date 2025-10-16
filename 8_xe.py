import math
import pygame, sys, random, numpy as np
from collections import deque

import heapq 
        
def sinh_trang_thai_bfs(ma_tran_dang_xet, hang_doi, hang, explored, ma_tran_cha):
    N = ma_tran_dang_xet.shape[0]
    for j in range(N):
        if ma_tran_dang_xet[:, j].sum() == 0:  
            con = ma_tran_dang_xet.copy(); con[hang, j] = 1
            con_bytes = con.tobytes()
            if con_bytes not in explored:
                hang_doi.append(con) 
                explored.add(con_bytes)
                ma_tran_cha[con_bytes] = ma_tran_dang_xet.tobytes()

def BFS(ma_tran_dich, trang_thai_ban_dau):
    hang_doi = deque([trang_thai_ban_dau])
    explored = {trang_thai_ban_dau.tobytes()} 
    ma_tran_cha = {trang_thai_ban_dau.tobytes(): None} 
    while hang_doi:
        ma_tran_dang_xet = hang_doi.popleft()
        if np.array_equal(ma_tran_dang_xet, ma_tran_dich):
            return ma_tran_dang_xet, ma_tran_cha
        for i in range(ma_tran_dang_xet.shape[0]):
            if 1 not in ma_tran_dang_xet[i]:
                sinh_trang_thai_bfs(ma_tran_dang_xet, hang_doi, i, explored, ma_tran_cha)
                break
    return None, ma_tran_cha

def truy_vet_BFS(ma_tran_cha, trang_thai_cuoi):
    duong_di = []
    dtype, shape = trang_thai_cuoi.dtype, trang_thai_cuoi.shape
    na = trang_thai_cuoi.tobytes()
    while na is not None:
        mang_1c = np.frombuffer(na, dtype=dtype); mang_2c = mang_1c.reshape(shape)
        duong_di.append(mang_2c)
        na = ma_tran_cha.get(na, None)
    return duong_di[::-1]

def tu_dong_BFS(ma_tran_dich, trang_thai_ban_dau):
    kq, cha_map = BFS(ma_tran_dich, trang_thai_ban_dau)
    if kq is None: return
    duong_di = truy_vet_BFS(cha_map, kq)
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]


def sinh_trang_thai_dfs(ma_tran_dang_xet, ngan_xep, hang, explored, ma_tran_cha):
    N = ma_tran_dang_xet.shape[0]
    for j in range(N):
        if ma_tran_dang_xet[:, j].sum() == 0:
            con = ma_tran_dang_xet.copy(); con[hang, j] = 1
            con_bytes = con.tobytes()
            if con_bytes not in explored:
                ngan_xep.append(con)  # xai stack
                explored.add(con_bytes)
                ma_tran_cha[con_bytes] = ma_tran_dang_xet.tobytes()

def DFS(ma_tran_dich, trang_thai_ban_dau):
    ngan_xep = [trang_thai_ban_dau]
    explored = {trang_thai_ban_dau.tobytes()}
    ma_tran_cha = {trang_thai_ban_dau.tobytes(): None}
    while ngan_xep:
        ma_tran_dang_xet = ngan_xep.pop()  
        if np.array_equal(ma_tran_dang_xet, ma_tran_dich):
            return ma_tran_dang_xet, ma_tran_cha
        for i in range(ma_tran_dang_xet.shape[0]):
            if 1 not in ma_tran_dang_xet[i]:
                sinh_trang_thai_dfs(ma_tran_dang_xet, ngan_xep, i, explored, ma_tran_cha)
                break
    return None, ma_tran_cha

def truy_vet_DFS(ma_tran_cha, trang_thai_cuoi):
    duong_di = []
    dtype, shape = trang_thai_cuoi.dtype, trang_thai_cuoi.shape
    na = trang_thai_cuoi.tobytes()
    while na is not None:
        mang_1c = np.frombuffer(na, dtype=dtype); mang_2c = mang_1c.reshape(shape)
        duong_di.append(mang_2c)
        na = ma_tran_cha.get(na, None)
    return duong_di[::-1]

def tu_dong_DFS(ma_tran_dich, trang_thai_ban_dau):
    kq, cha_map = DFS(ma_tran_dich, trang_thai_ban_dau)
    if kq is None: return
    duong_di = truy_vet_DFS(cha_map, kq)
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]



def tinh_cost(ma_tran, row, col, vi_tri_dich):
    cost = 1
    
    for r, c in vi_tri_dich:
        if r == row:
            cost += abs(col - c)
            break
    return cost


def UCS(start, Ma_Tran_Dich, vi_tri_dich):
    pq = []
    counter = 0
    heapq.heappush(pq, (0, counter, start.copy()))
    parent = {start.tobytes(): None}
    best_cost = {start.tobytes(): 0}
    node_count = 0

    while pq:
        cost, _, state = heapq.heappop(pq)
        key = state.tobytes()
        node_count += 1

        if best_cost.get(key, float('inf')) != cost:
            continue

        print(f"\nNode #{node_count}: Tổng chi phí = {cost}")
        print("Trạng thái hiện tại:")
        print(state)

        if np.array_equal(state, Ma_Tran_Dich):
            print(f"Tổng chi phí cuối: {cost}")
            return state, parent, best_cost, cost

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
            new_cost = cost + step_cost

            child_key = child.tobytes()
            if new_cost < best_cost.get(child_key, float('inf')):
                best_cost[child_key] = new_cost
                parent[child_key] = state
                counter += 1
                heapq.heappush(pq, (new_cost, counter, child))
                print(f"  Sinh trạng thái con: đặt xe tại ({row}, {col}), step_cost = {step_cost}, tổng cost = {new_cost}")

    print(f"\nKHÔNG TÌM THẤY ĐÍCH sau {node_count} node")
    return None, parent, best_cost, None

def truy_vet_UCS(parent, trang_thai_cuoi):
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


def sinh_trang_thai_dls(ma_tran_dang_xet, hang, explored, ma_tran_cha, limit, depth):
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


def DLS(ma_tran_dich, trang_thai_ban_dau, limit):
    stack = [(trang_thai_ban_dau, 0)]  
    explored = {trang_thai_ban_dau.tobytes()}
    ma_tran_cha = {trang_thai_ban_dau.tobytes(): None}

    while stack:
        ma_tran_dang_xet, depth = stack.pop()

        if np.array_equal(ma_tran_dang_xet, ma_tran_dich):
            return ma_tran_dang_xet, ma_tran_cha

       
        for i in range(ma_tran_dang_xet.shape[0]):
            if 1 not in ma_tran_dang_xet[i]:
                children = sinh_trang_thai_dls(ma_tran_dang_xet, i, explored, ma_tran_cha, limit, depth + 1)
                for child in reversed(children):  # LIFO
                    stack.append((child, depth + 1))
                break
    return None, ma_tran_cha


def truy_vet_DLS(ma_tran_cha, trang_thai_cuoi):
    duong_di = []
    dtype, shape = trang_thai_cuoi.dtype, trang_thai_cuoi.shape
    na = trang_thai_cuoi.tobytes()
    while na is not None:
        mang_1c = np.frombuffer(na, dtype=dtype)
        mang_2c = mang_1c.reshape(shape)
        duong_di.append(mang_2c)
        na = ma_tran_cha.get(na, None)
    return duong_di[::-1]


def tu_dong_DLS(ma_tran_dich, trang_thai_ban_dau, limit=8):

    kq, cha_map = DLS(ma_tran_dich, trang_thai_ban_dau, limit)
    if kq is None:
        return
    duong_di = truy_vet_DLS(cha_map, kq)
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]

def IDS(ma_tran_dich, trang_thai_ban_dau, N=8):
    """ IDS: Lặp depth limit từ 0 -> N, mỗi lần gọi lại DLS """
    for limit in range(N+1):
       
        kq, cha_map = DLS(ma_tran_dich, trang_thai_ban_dau, limit)
        if kq is not None:
            return kq, cha_map
    return None, {}  

def tu_dong_IDS(ma_tran_dich, trang_thai_ban_dau, N=8):
    kq, cha_map = IDS(ma_tran_dich, trang_thai_ban_dau, N)
    if kq is None:
        return
    duong_di = truy_vet_DLS(cha_map, kq)  
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]

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


def greedy_search(start, Ma_Tran_Dich, vi_tri_dich):
    pq = []
    counter = 0
    heapq.heappush(pq, (heuristic(start), 0, counter, start.copy()))  
    visited = {start.tobytes()}
    parent = {start.tobytes(): None}
    best_cost = {start.tobytes(): 0} 
    node_count = 0

    print("Bắt đầu GREEDY SEARCH")
    print(f"Trạng thái ban đầu (cost=0, h={heuristic(start)}):")
    print(start)
    print(f"Dest (vi_tri_dich): {vi_tri_dich}")

    while pq:
        h, cost, _, state = heapq.heappop(pq)
        key = state.tobytes()
        node_count += 1

        print(f"\nNode #{node_count}: cost={cost}, h={h}")
        print("Trạng thái hiện tại:")
        print(state)

        if np.array_equal(state, Ma_Tran_Dich):
            print(f"\nTÌM THẤY ĐÍCH sau {node_count} node!")
            print(f"Tổng chi phí cuối: {cost}, h=0")
            print(f"Dest (vi_tri_dich): {vi_tri_dich}")
            return state, parent, best_cost, cost

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
            new_state = state.copy()
            new_state[row, col] = 1
            child_key = new_state.tobytes()
            if child_key not in visited:
                visited.add(child_key)
                parent[child_key] = state
                step_cost = tinh_cost(new_state, row, col, vi_tri_dich)
                new_cost = cost + step_cost
                best_cost[child_key] = new_cost
                new_h = heuristic(new_state)
                counter += 1
                heapq.heappush(pq, (new_h, new_cost, counter, new_state))
                print(f"  Sinh trạng thái con: đặt xe tại ({row}, {col}), step_cost={step_cost} (khoảng cách={abs(col - [c for r, c in vi_tri_dich if r == row][0] if [r for r, c in vi_tri_dich if r == row] else 0)}), cost={new_cost}, h={new_h}")

    print(f"\nKHÔNG TÌM THẤY ĐÍCH sau {node_count} node")
    return None, {}, {}, None

def tu_dong_greedy_1(Ma_Tran_Dich, start, vi_tri_dich, N=8):
    kq, parent, best_cost, tong_cost = greedy_search(start, Ma_Tran_Dich, vi_tri_dich)
    if kq is None:
        return
    duong_di = []
    state = kq
    while state is not None:
        duong_di.append(state)
        state = parent.get(state.tobytes(), None)
    duong_di.reverse()
    print(f"Đường đi GREEDY: {len(duong_di)} trạng thái, Tổng chi phí: {tong_cost}")
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]

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

  
def hill_climbing(start, Ma_Tran_Dich):
    current_board = start.copy()
    current_heuristic = heuristic(current_board)
    path = [current_board.copy()]
    
    while True:
        neighbors = []
        n = current_board.shape[0]
        rook_positions = [(r, c) for r in range(n) for c in range(n) if current_board[r, c] == 1]

        for r, c in rook_positions:
            for new_c in range(n):
                if new_c != c and current_board[r, new_c] == 0:
                    neighbor = current_board.copy()
                    neighbor[r, c] = 0
                    neighbor[r, new_c] = 1
                    neighbors.append(neighbor)
            for new_r in range(n):
                if new_r != r and current_board[new_r, c] == 0:
                    neighbor = current_board.copy()
                    neighbor[r, c] = 0
                    neighbor[new_r, c] = 1
                    neighbors.append(neighbor)

        best_neighbor = current_board
        best_heuristic = current_heuristic
        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < best_heuristic:
                best_heuristic = h
                best_neighbor = neighbor

        if best_heuristic >= current_heuristic:
            break

        current_board = best_neighbor
        current_heuristic = best_heuristic
        path.append(current_board.copy())

        if np.array_equal(current_board, Ma_Tran_Dich):
            break
    
    return path


def tu_dong_hill_climbing(Ma_Tran_Dich, start):
    path = hill_climbing(start, Ma_Tran_Dich)
    for state in path:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]



def tinh_fitness(ca_the, Ma_Tran_Dich):
    N = len(ca_the)
    diem = 0
    for r in range(N):
        cot_dung = np.where(Ma_Tran_Dich[r] == 1)[0][0]
        if ca_the[r] == cot_dung:
            diem += 1
    return diem

def genetic_search(Ma_Tran_Dich, N=8, so_ca_the=200, xac_suat_dot_bien=0.1, max_the_he=500):

    quan_the = [np.random.randint(N, size=N) for _ in range(so_ca_the)]
    lich_su = []  

    for the_he in range(max_the_he):
       
        fitness = [tinh_fitness(ca_the, Ma_Tran_Dich) for ca_the in quan_the]

       
        best_idx = np.argmax(fitness)
        best_ca_the = quan_the[best_idx]
        lich_su.append(best_ca_the.copy())

        if fitness[best_idx] == N:
            return best_ca_the, lich_su

        tong_fit = sum(fitness)
        if tong_fit == 0:
            xs_chon = [1/so_ca_the] * so_ca_the
        else:
            xs_chon = [f/tong_fit for f in fitness]

        
        quan_the_moi = []
        for _ in range(so_ca_the//2):
            bo = quan_the[np.random.choice(range(so_ca_the), p=xs_chon)]
            me = quan_the[np.random.choice(range(so_ca_the), p=xs_chon)]
            diem_cat = random.randint(1, N-1)
            con1 = np.concatenate((bo[:diem_cat], me[diem_cat:]))
            con2 = np.concatenate((me[:diem_cat], bo[diem_cat:]))
            quan_the_moi.extend([con1, con2])

        for ca_the in quan_the_moi:
            if random.random() < xac_suat_dot_bien:
                pos = random.randint(0, N-1)
                ca_the[pos] = random.randint(0, N-1)

        quan_the = quan_the_moi

    return None, lich_su

def tu_dong_Genetic(Ma_Tran_Dich, N=8):
    kq, lich_su = genetic_search(Ma_Tran_Dich, N)
    if kq is None:
        return

    for ca_the in lich_su:
        yield [(r, ca_the[r]) for r in range(N)]

def heuristic_1(board, goal):
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
    frontier = [(heuristic_1(start, goal), start)]
    explored = {start.tobytes(): None}

    while frontier:
        frontier.sort(key=lambda x: x[0])
        frontier = frontier[:k]
        new_frontier = []

        for _, state in frontier:
            if np.array_equal(state, goal):
                print("Đã đạt trạng thái đích!")
                return state, explored

            children = sinh_trang_thai_beam(state, goal)
            for child in children:
                b = child.tobytes()
                if b not in explored:
                    explored[b] = state.tobytes()
                    new_frontier.append((heuristic_1(child, goal), child))

        if not new_frontier:
            print("Không còn trạng thái con!")
            break
        frontier = new_frontier

    print("Beam Search không tìm thấy lời giải!")
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
        print(" Không tìm thấy giải pháp!")
        return
    duong_di = truy_vet(cha_map, kq)
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0])
                        for c in range(state.shape[1])
                        if state[r, c] == 1]

        

import numpy as np, random, math

def tinh_cost_1(board, goal):
    return int(np.sum(np.abs(board - goal)))

def tao_start_tu_goal(goal):
    n = goal.shape[0]
    need = int(goal.sum())
    start = np.zeros_like(goal)
    cells = [(r, c) for r in range(n) for c in range(n)]
    random.shuffle(cells)
    for i in range(need):
        r, c = cells[i]
        start[r, c] = 1
    return start

def neighbor_any(board):
    n = board.shape[0]
    new_board = board.copy()
    rook_positions = [(r,c) for r in range(n) for c in range(n) if board[r,c]==1]
    empty_positions = [(r,c) for r in range(n) for c in range(n) if board[r,c]==0]
    if not rook_positions or not empty_positions:
        return new_board
    r0,c0 = random.choice(rook_positions)
    r1,c1 = random.choice(empty_positions)
    new_board[r0,c0] = 0
    new_board[r1,c1] = 1
    return new_board

def simulated_annealing(start_board, goal_board, T=1000.0, cooling_rate=0.995, max_iter=10000):
    # ensure start has same number of rooks as goal
    if start_board.sum() != goal_board.sum() or start_board.sum() == 0:
        start_board = tao_start_tu_goal(goal_board)

    current = start_board.copy()
    current_cost = tinh_cost_1(current, goal_board)
    history = [current.copy()]

    print("SA start cost:", current_cost)

    for step in range(max_iter):
        if np.array_equal(current, goal_board) or current_cost == 0:
            print(f"Reached goal at step {step}, cost={current_cost}")
            break

        new_state = neighbor_any(current)
        new_cost = tinh_cost_1(new_state, goal_board)
        delta = new_cost - current_cost

        # debug occasional
        if step % 200 == 0:
            print(f"step {step}: cost {current_cost} -> {new_cost}, T={T:.4f}")

        if delta < 0 or random.random() < math.exp(-delta / T if T>0 else 0):
            current, current_cost = new_state, new_cost
            history.append(current.copy())

        T *= cooling_rate
        if T < 1e-8:
            break

    return current, history

def tu_dong_SA(goal_board, start_board, T=200, cooling_rate=0.97, max_iter=5000):
    current, history = simulated_annealing(start_board, goal_board, T, cooling_rate, max_iter)
    # debug final
    print(" cost cuối cùng:", tinh_cost_1(current, goal_board), "history len:", len(history))
    for state in history:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]




# ===== AND-OR SEARCH cho 8 quân xe =====
def next_row(board):
    """Tìm hàng đầu tiên chưa có xe"""
    for r in range(board.shape[0]):
        if 1 not in board[r]:
            return r
    return None

def and_or_search(state, goal, n=8):
    plan = or_search(state, goal, n, {})
    return plan

def or_search(state, goal, n, visited):
    if np.array_equal(state, goal):
        return "Thành công"

    key = state.tobytes()
    if key in visited:
        return None
    visited[key] = True

    r = next_row(state)
    if r is None:
        return None

    for c in range(n):
        if state[:, c].sum() == 0:  
            new_state = state.copy()
            new_state[r, c] = 1
            plan = and_search(new_state, goal, n, visited)
            if plan is not None:
                return ((r, c), plan) 

    return None

def and_search(state, goal, n, visited):
    """AND node: tiếp tục tìm kế hoạch ở hàng tiếp theo"""
    return or_search(state, goal, n, visited)

def tu_dong_ANDOR(goal_board, start_board):
    plan = and_or_search(start_board, goal_board)
    if plan is None:
        print("Không tìm thấy kế hoạch (AND-OR thất bại).")
        return

    def traverse(plan, state):
        if plan == "Thành công":
            yield state
        elif isinstance(plan, tuple) or isinstance(plan, list):
            (r, c), subplan = plan
            new_state = state.copy()
            new_state[r, c] = 1
            yield new_state
            for s in traverse(subplan, new_state):
                yield s

    for s in traverse(plan, start_board.copy()):
        yield [(r, c) for r in range(s.shape[0]) for c in range(s.shape[1]) if s[r, c] == 1]

def sinh_trang_thai_hang(board):
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

def BFS_non(Ma_Tran_Dich, Trang_Thai_BanDau, heuristic, max_depth=20):
    pq = []  
    counter = 0
    heapq.heappush(pq, (heuristic(Trang_Thai_BanDau), counter, Trang_Thai_BanDau, []))
    counter += 1
    visited = set()

    while pq:
        _, _, board, path = heapq.heappop(pq)

        if np.array_equal(board, Ma_Tran_Dich):
            return path + [board]

        key = board.tobytes()
        if key in visited:
            continue
        visited.add(key)

        if len(path) >= max_depth:
            continue

        for next_board in sinh_trang_thai_hang(board):
            next_key = next_board.tobytes()
            if next_key not in visited:
                h = heuristic(next_board)
                heapq.heappush(pq, (h, counter, next_board, path + [board]))
                counter += 1

    return None


def tu_dong_BFS_non(Ma_Tran_Dich, Trang_Thai_BanDau):
    def heuristic(board):
        return np.sum(board != Ma_Tran_Dich)  
    return BFS_non(Ma_Tran_Dich, Trang_Thai_BanDau, heuristic)

N=8
def khong_tan_cong(pos, quan_co):
    r, c = pos
    for (r2, c2) in quan_co:
        if r == r2 or c == c2:
            return False
    return True

def sinh_trang_thai(trang_thai, co_dinh):
    quan_hien_tai = trang_thai.copy()

    if len(quan_hien_tai) < N:
        for r in range(N):
            for c in range(N):
                pos = (r, c)
                if pos in quan_hien_tai or pos == co_dinh:
                    continue
                if khong_tan_cong(pos, quan_hien_tai):
                    yield quan_hien_tai + [pos]

    for i, (r_old, c_old) in enumerate(quan_hien_tai):
        if (r_old, c_old) == co_dinh:
            continue
        for r in range(N):
            for c in range(N):
                pos = (r, c)
                if pos in quan_hien_tai:
                    continue
                if khong_tan_cong(pos, [q for j, q in enumerate(quan_hien_tai) if j != i]):
                    trang_moi = quan_hien_tai.copy()
                    trang_moi[i] = pos
                    yield trang_moi

def BFS_8quanxe(co_dinh):
    start = [co_dinh]
    frontier = deque([(start, [start])])
    visited = set()
    visited.add(tuple(start))

    while frontier:
        trang_thai, lich_su = frontier.popleft()
        if len(trang_thai) == N:
            return trang_thai, lich_su

        for trang_moi in sinh_trang_thai(trang_thai, co_dinh):
            trang_tuple = tuple(sorted(trang_moi))
            if trang_tuple not in visited:
                visited.add(trang_tuple)
                frontier.append((trang_moi, lich_su + [trang_moi]))
    return None, []

def in_ban_co(state):
    board = np.zeros((N, N), dtype=int)
    for (r, c) in state:
        board[r][c] = 1
    for row in board:
        print(" ".join(str(x) for x in row))
    print("-" * 30)

def tu_dong_BFS_par(co_dinh):
    goal, history = BFS_8quanxe(co_dinh)
    if goal is None:
        print(" Không tìm thấy lời giải!")
        return

    print(" BFS đã tìm thấy lời giải! Đường đi có", len(history), "bước.")
    for i, state in enumerate(history):
        print("Bước", i, ":", state)
        in_ban_co(state)
        yield state

import itertools

def kiem_tra_rang_buoc(assignments):
    values = list(assignments.values())

    if len(values) != len(set(values)):
        return False

    for (r1, c1), (r2, c2) in itertools.combinations(values, 2):
        if r1 == r2 or c1 == c2:
            return False
    return True

def backtracking(assignments, variables, domains):
    if len(assignments) == len(variables):
        return assignments

    var = variables[len(assignments)]
    for value in domains[var]:
        new_assignments = assignments.copy()
        new_assignments[var] = value

        if kiem_tra_rang_buoc(new_assignments):
            result = backtracking(new_assignments, variables, domains)
            if result is not None:
                return result
    return None
def tu_dong_CSP():
    variables = [f"X{i}" for i in range(8)]
    domain_all = [(r, c) for r in range(8) for c in range(8)]
    domains = {var: list(domain_all) for var in variables}

    stack = [({}, 0)]
    while stack:
        assignments, idx = stack.pop()
        if idx == len(variables):
            yield list(assignments.values()) 
            return

        var = variables[idx]
        for value in domains[var]:
            new_assign = assignments.copy()
            new_assign[var] = value

            if kiem_tra_rang_buoc(new_assign):
                yield list(new_assign.values())  
                stack.append((new_assign, idx + 1))

import itertools
import copy

def kiem_tra_rang_buoc(assignments):
    values = list(assignments.values())
    if len(values) != len(set(values)):
        return False
    for (r1, c1), (r2, c2) in itertools.combinations(values, 2):
        if r1 == r2 or c1 == c2:
            return False
    return True


def forward_checking(assignments, variables, domains):
   
    if len(assignments) == len(variables):
        return assignments

 
    var = variables[len(assignments)]

    for value in domains[var]:
        new_assign = assignments.copy()
        new_assign[var] = value

        if kiem_tra_rang_buoc(new_assign):
            
            new_domains = copy.deepcopy(domains)

            r_val, c_val = value
            for other_var in variables[len(assignments) + 1:]:
                if value in new_domains[other_var]:
                    new_domains[other_var].remove(value)
                new_domains[other_var] = [
                    (r, c)
                    for (r, c) in new_domains[other_var]
                    if r != r_val and c != c_val
                ]

                if not new_domains[other_var]:
                    break
            else:
                result = forward_checking(new_assign, variables, new_domains)
                if result is not None:
                    return result
    return None


def tu_dong_CSP_forward_checking():
    variables = [f"X{i}" for i in range(8)]
    domain_all = [(r, c) for r in range(8) for c in range(8)]
    domains = {var: list(domain_all) for var in variables}

    stack = [({}, domains, 0)]
    while stack:
        assignments, doms, idx = stack.pop()

        if idx == len(variables):
            yield list(assignments.values())
            return

        var = variables[idx]
        for value in doms[var]:
            new_assign = assignments.copy()
            new_assign[var] = value

            if kiem_tra_rang_buoc(new_assign):
                new_doms = copy.deepcopy(doms)
                r_val, c_val = value
                for other_var in variables[idx + 1:]:
                    new_doms[other_var] = [
                        (r, c)
                        for (r, c) in new_doms[other_var]
                        if r != r_val and c != c_val
                    ]
                yield list(new_assign.values()) 
                stack.append((new_assign, new_doms, idx + 1))
pygame.init()
kt_hvuong, kt_ban, khoang_cach_2ban = 40, 8, 150
win_rong, win_dai = 1200, 700
screen = pygame.display.set_mode((win_rong, win_dai))
pygame.display.set_caption("Game 8 xe")

nen = pygame.image.load("bg2.png"); nen = pygame.transform.scale(nen, (win_rong, win_dai))
xe = pygame.image.load("xe.png"); xe = pygame.transform.scale(xe, (kt_hvuong, kt_hvuong))
font = pygame.font.SysFont(None, 40)

def xep_phai(n=8):
    cols = list(range(n)); kq = []
    for row in range(n):
        col = random.choice(cols); kq.append((row, col)); cols.remove(col)
    return kq

def ve_ban_co(x_start, y_start, vi_tri):
    for row in range(kt_ban):
        for col in range(kt_ban):
            x = x_start + col * kt_hvuong; y = y_start + row * kt_hvuong
            color = (255, 255, 255) if (row+col)%2==0 else (55,53,62)
            pygame.draw.rect(screen, color, (x,y,kt_hvuong,kt_hvuong))
            if vi_tri and (row,col) in vi_tri: screen.blit(xe,(x,y))

def ve_button(text,x,y,w,h,color,hover_color,vi_tri_chuot):
    mouse_x, mouse_y = vi_tri_chuot
    hover = (x<=mouse_x<=x+w) and (y<=mouse_y<=y+h)
    pygame.draw.rect(screen, hover_color if hover else color, (x,y,w,h), border_radius=12)
    pygame.draw.rect(screen, (0,0,0), (x,y,w,h), 2, border_radius=12)
    label = font.render(text, True, (0,0,0))
    screen.blit(label,(x+(w-label.get_width())//2,y+(h-label.get_height())//2))
    return hover

############### GAME LOOP 
dang_xet="menu"; thuat_toan=None; vi_tri_xe=None
tu_dong_bfs=None; cap_nhat_bfs=[]
tu_dong_dfs=None; cap_nhat_dfs=[]
tu_dong_ucs=None; cap_nhat_ucs=[]
tu_dong_dls=None; cap_nhat_dls=[]
tu_dong_ids=None; cap_nhat_ids=[]
tu_dong_greedy=None; cap_nhat_greedy=[]
tu_dong_a_star = None;cap_nhat_a_star = []
tu_dong_hill = None;cap_nhat_hill = []
tu_dong_genetic = None;cap_nhat_genetic = []
tu_dong_beam = None;cap_nhat_beam = []
tu_dong_sa = None;cap_nhat_sa = []
tu_dong_andor = None; cap_nhat_andor = []
tu_dong_bfs_non = None; cap_nhat_bfs_non = []
tu_dong_bfs_par = None;cap_nhat_bfs_par = []
tu_dong_csp = None; cap_nhat_csp = []
tu_dong_forward = None; cap_nhat_forward = []


clock=pygame.time.Clock()
step_delay=1500; last_step_time=pygame.time.get_ticks()
rong_ban=kt_ban*kt_hvuong*2+khoang_cach_2ban; dai_ban=kt_ban*kt_hvuong

while True:
    vi_tri_chuot=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT: pygame.quit(); sys.exit()
        if dang_xet=="menu" and event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            x, y = vi_tri_chuot
            if 200 <= x <= 500 and 60 <= y <= 110:  
                thuat_toan="BFS"; vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                tu_dong_bfs=tu_dong_BFS(Ma_Tran_Dich,Trang_Thai_Mang)
                dang_xet="game"

            elif 200 <= x <= 500 and 120 <= y <= 170:  
                thuat_toan="DFS"; vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                tu_dong_dfs=tu_dong_DFS(Ma_Tran_Dich,Trang_Thai_Mang)
                dang_xet="game"

            elif 200 <= x <= 500 and 180 <= y <= 230:  
                thuat_toan="UCS"
                vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                kq, parent, visited, tong_cost = UCS(Trang_Thai_Mang, Ma_Tran_Dich, vi_tri_xe)
                print("Tổng chi phí UCS =", tong_cost)  
                duong_di = truy_vet_UCS(parent, kq)
                tu_dong_ucs = iter([
                    [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]
                    for state in duong_di
                ])
                cap_nhat_ucs = []
                dang_xet="game"

            elif 200 <= x <= 500 and 240 <= y <= 290:  
                thuat_toan="DLS"
                vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                tu_dong_dls=tu_dong_DLS(Ma_Tran_Dich,Trang_Thai_Mang,limit=8)
                cap_nhat_dls=[]
                dang_xet="game"

            elif 200 <= x <= 500 and 300 <= y <= 350:  
                thuat_toan="IDS"
                vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                tu_dong_ids=tu_dong_IDS(Ma_Tran_Dich,Trang_Thai_Mang,N=8)
                cap_nhat_ids=[]
                dang_xet="game"

            elif 200 <= x <= 500 and 360 <= y <= 410:  
                thuat_toan="GREEDY"
                vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                print("vi_tri_dich:", vi_tri_xe)
                kq, parent, visited, tong_cost = greedy_search(Trang_Thai_Mang, Ma_Tran_Dich, vi_tri_xe)
                print("Tổng chi phí GREEDY =", tong_cost)
                tu_dong_greedy = tu_dong_greedy_1(Ma_Tran_Dich, Trang_Thai_Mang, vi_tri_xe, N=8)
                cap_nhat_greedy=[]
                dang_xet="game"

            elif 200 <= x <= 500 and 420 <= y <= 470:  
                thuat_toan="A*"
                vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                kq, parent, visited, tong_cost = A_star(Trang_Thai_Mang, Ma_Tran_Dich, vi_tri_xe)
                print("Tổng chi phí A* =", tong_cost)
                duong_di = truy_vet_A_star(parent, kq)
                tu_dong_a_star = iter([
                    [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]
                    for state in duong_di
                ])
                cap_nhat_a_star=[]
                dang_xet="game"

            elif 200 <= x <= 500 and 480 <= y <= 530:  
                thuat_toan="HILL CLIMBING"
                vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                tu_dong_hill=tu_dong_hill_climbing(Ma_Tran_Dich,Trang_Thai_Mang)
                cap_nhat_hill=[]
                dang_xet="game"

            elif 200 <= x <= 500 and 540 <= y <= 590:  
                thuat_toan="GENETIC"
                vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                tu_dong_genetic=tu_dong_Genetic(Ma_Tran_Dich,N=8)
                cap_nhat_genetic=[]
                dang_xet="game"
            elif 200 <= x <= 500 and 600 <= y <= 650:  # Button BEAM
                thuat_toan = "BEAM"
                vi_tri_xe = xep_phai()  # Tạo bàn bên phải (goal)
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)
                tu_dong_beam = tu_dong_Beam(Ma_Tran_Dich, Trang_Thai_Mang, k=3)  # k=3 hoặc tăng lên nếu cần
                cap_nhat_beam = []
                dang_xet = "game"
            elif 550 <= x <= 850 and 60 <= y <= 110:  # Button SA
                thuat_toan = "SA"
                vi_tri_xe = xep_phai()  # tạo goal (bàn bên phải)
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)  # bàn bên trái trống
                tu_dong_sa = tu_dong_SA(Ma_Tran_Dich, Trang_Thai_Mang)
                cap_nhat_sa = []
                dang_xet = "game"

            elif 550 <= x <= 850 and 120 <= y <= 170:  # Button AND-OR
                thuat_toan = "AND-OR"
                vi_tri_xe = xep_phai()  # Tạo bàn bên phải (goal)
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)  # Bàn bên trái trống
                tu_dong_andor = tu_dong_ANDOR(Ma_Tran_Dich, Trang_Thai_Mang)
                cap_nhat_andor = []
                dang_xet = "game"
            elif 550 <= x <= 850 and 180 <= y <= 230:  # Button BFS_non
                thuat_toan = "BFS_non"
                vi_tri_xe = xep_phai()  # Tạo bàn bên phải (goal)
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)  # Bàn bên trái trống
                cap_nhat_bfs_non = tu_dong_BFS_non(Ma_Tran_Dich, Trang_Thai_Mang)  # Chạy BFS_non
                dang_xet = "game"
            elif 550 <= x <= 850 and 240 <= y <= 290:  # Button BFS_par
                thuat_toan = "BFS_PAR"
                co_dinh = (3, 5)  # ví dụ cố định quân ở (3,5), sau này bạn có thể random/cho click chuột
                tu_dong_bfs_par = tu_dong_BFS_par(co_dinh)
                cap_nhat_bfs_par = []
                dang_xet = "game"
            elif 550 <= x <= 850 and 300 <= y <= 350:  # Button CSP
                thuat_toan = "CSP"
                vi_tri_xe = xep_phai()  # Tạo bàn bên phải (goal)
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)  # Bàn bên trái trống

                tu_dong_csp = tu_dong_CSP()  # Generator tạo từng bước trạng thái
                cap_nhat_csp = []  # Danh sách chứa các trạng thái trung gian để vẽ
                dang_xet = "game"
            elif 550 <= x <= 850 and 360 <= y <= 410:  # Button Forward Checking
                thuat_toan = "ForwardChecking"
                vi_tri_xe = xep_phai()  # tạo bàn bên phải (goal)
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)  # bàn bên trái trống

                tu_dong_forward = tu_dong_CSP_forward_checking()  # tạo generator FC
                cap_nhat_forward = []  # danh sách lưu trạng thái
                dang_xet = "game"
                print("Bắt đầu giải bằng Forward Checking...")





         

        elif dang_xet=="game" and event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            dang_xet="menu"

    screen.blit(nen,(0,0))
    if dang_xet=="menu":
        ve_button("BFS",200,60,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("DFS",200,120,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("UCS",200,180,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("DLS",200,240,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("IDS",200,300,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("GREEDY",200,360,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("A*",200,420,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("HILL CLIMBING", 200, 480, 300, 50, (255, 253, 181), (150, 150, 150), vi_tri_chuot)
        ve_button("GENETIC", 200, 540, 300, 50, (255, 253, 181), (150, 150, 150), vi_tri_chuot)
        ve_button("BEAM", 200, 600, 300, 50, (255, 253, 181), (150, 150, 150), vi_tri_chuot)
        ve_button("SIMULATED ANNEALING", 550, 60, 350, 50, (255, 253, 181), (150,150,150), vi_tri_chuot)
        ve_button("AND-OR", 550, 120, 300, 50, (255,253,181), (150,150,150), vi_tri_chuot)
        ve_button("BFS_non", 550, 180, 300, 50, (255,253,181), (150,150,150), vi_tri_chuot)
        ve_button("BFS_par", 550, 240, 300, 50, (255,253,181), (150,150,150), vi_tri_chuot)
        ve_button("CSP BACKTRACKING", 550, 300, 300, 50, (255,253,181), (150,150,150), vi_tri_chuot)
        ve_button("FORWARD CHECKING", 550, 360, 300, 50, (255,253,181), (150,150,150), vi_tri_chuot)
        
    elif dang_xet=="game":
        now=pygame.time.get_ticks()
        if thuat_toan=="BFS":
            if now-last_step_time>step_delay:
                try: cap_nhat_bfs=next(tu_dong_bfs)
                except: pass
                last_step_time=now
            x_ban=(win_rong-rong_ban)//2; y_ban=(win_dai-dai_ban)//2
            ve_ban_co(x_ban,y_ban,cap_nhat_bfs)
            ve_ban_co(x_ban+kt_ban*kt_hvuong+khoang_cach_2ban,y_ban,vi_tri_xe)
        elif thuat_toan=="DFS":
            if now-last_step_time>step_delay:
                try: cap_nhat_dfs=next(tu_dong_dfs)
                except: pass
                last_step_time=now
            x_ban=(win_rong-rong_ban)//2; y_ban=(win_dai-dai_ban)//2
            ve_ban_co(x_ban,y_ban,cap_nhat_dfs)
            ve_ban_co(x_ban+kt_ban*kt_hvuong+khoang_cach_2ban,y_ban,vi_tri_xe)
        elif thuat_toan == "UCS":
            if now - last_step_time > step_delay:
                try: cap_nhat_ucs = next(tu_dong_ucs)
                except: pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2; y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_ucs)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)
        elif thuat_toan == "DLS":
            if now - last_step_time > step_delay:
                try: cap_nhat_dls = next(tu_dong_dls)
                except: pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2; y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_dls)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "IDS":
            if now - last_step_time > step_delay:
                try: cap_nhat_ids = next(tu_dong_ids)
                except: pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2; y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_ids)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "GREEDY":
            if now - last_step_time > step_delay:
                try: cap_nhat_greedy = next(tu_dong_greedy)
                except: pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2; y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_greedy)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "A*":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_a_star = next(tu_dong_a_star)
                except:
                    pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_a_star)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "HILL CLIMBING":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_hill = next(tu_dong_hill)
                except:
                    pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_hill)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "GENETIC":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_genetic = next(tu_dong_genetic)
                except:
                    pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_genetic)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "BEAM":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_beam = next(tu_dong_beam)
                except StopIteration:
                    pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_beam)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)
        elif thuat_toan == "SA":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_sa = next(tu_dong_sa)
                except:
                    pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_sa)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)
        elif thuat_toan == "AND-OR":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_andor = next(tu_dong_andor)
                except:
                    pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_andor)        # Bàn bên trái chạy thuật toán
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)  # Bàn bên phải (goal)
        elif thuat_toan == "BFS_non":
            if now - last_step_time > step_delay:
                try:
                    if cap_nhat_bfs_non:
                        cap_nhat_bfs_non = [cap_nhat_bfs_non.pop(0)]
                except:
                    pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_bfs_non)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif dang_xet == "game":
            now = pygame.time.get_ticks()
            if thuat_toan == "BFS_PAR":
                if now - last_step_time > step_delay:
                    try:
                        cap_nhat_bfs_par = next(tu_dong_bfs_par)
                    except StopIteration:
                        pass
                    last_step_time = now
                x_ban = (win_rong - rong_ban) // 2
                y_ban = (win_dai - dai_ban) // 2
                ve_ban_co(x_ban, y_ban, cap_nhat_bfs_par)  
                ve_ban_co(x_ban + kt_ban*kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)  
        elif thuat_toan == "CSP":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_csp = next(tu_dong_csp)
                except:
                    pass
                last_step_time = now

            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_csp)                 
            ve_ban_co(x_ban + kt_ban*kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe) 
        elif thuat_toan == "ForwardChecking":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_forward = next(tu_dong_forward)
                except StopIteration:
                    pass
                last_step_time = now
    
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2

           
            ve_ban_co(x_ban, y_ban, cap_nhat_forward)

           
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)





    pygame.display.update(); clock.tick(30)