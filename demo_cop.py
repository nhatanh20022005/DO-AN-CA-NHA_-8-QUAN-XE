
import pygame, sys, random, numpy as np
from collections import deque

import heapq # qly hang đợi ưu tiên, để lấy chi phí rẻ nhất
# Iterative Deeping: theo DFS ( lifo) , tìm kiếm sâu dần ko đệ quy, 
# C1: chạy for ở ngoài, bên trong bê nguyên DFS xuống, độ sau của trạng thái sinh ra có nằm trong độ sâu cho trước
# C2: bê DLS xuống sửa lại

###Informed Search: BFS(greedy search, Heuristic: ước lượng chi phí trạng thái đang xét đến tt mục tiêu, A* search)
# gx = fx + hx ( cost + heuristics); hx<= h'x ( h'x: chi phí thực tế)
# heu(có nhìu cách, ko thể trùng nhau, tùy thuộc vào bài toán): hx = (8 - số hàng bị đặt) + (8 - số cột bị đặt) nên ta lấy càng thấp càng tốt, còn chưa bị đặt thì lấy càng cao càng tốt, có thể có cách tính hx tốt hơn
##Greedy search: trạng thái lưu trữ là hàng đợi ưu tiên, chi phí hiện tại đến tt mục tiêu, chưa xảy ra nhưng mình ước lượng
## A*: trước đó có hàm tính cost và heuristic, và hàm chi phí 2 cái trên ròi mới tới A*
## xây dựng hàm heuristic : dựa vào kinh nghiệm
## tạo pq,cứ 1 hành động lên trạng thái đang xét thì sinh ra trạng thái, dừng khi pq rỗng, tìm thấy thì xuất solution
# sau buổi này làm thêm: IDS, greedy, A*


#########các thuật toán Local Search
##Hill Climbing (Leo đồi):(khó tìm ra giải pháp):từ tt đang xét, sinh ra các tt tiếp theo, chon tt mà heu tốt nhất và phải tốt hơn cái đang xét, cho đến khi tìm thấy mục tiêu
#tối ưu về mặt lưu trữ vì nó chỉ lưu heu của ma trận sinh ra từ tt đang xét
# hạn chế: dễ rơi vào tối ưu cục bộ 

# chỉ quan tâm tới lân cận của tt đang xét
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
    explored = {trang_thai_ban_dau.tobytes()} #chuyển ma trận thành chuỗi bytes, vì NumPy array không hash được trực tiếp
    ma_tran_cha = {trang_thai_ban_dau.tobytes(): None} #dict
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

def run_BFS_generator(ma_tran_dich, trang_thai_ban_dau):
    kq, cha_map = BFS(ma_tran_dich, trang_thai_ban_dau)
    if kq is None: return
    duong_di = truy_vet_BFS(cha_map, kq)
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]

######################
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
        ma_tran_dang_xet = ngan_xep.pop()  # khác BFS
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

def run_DFS_generator(ma_tran_dich, trang_thai_ban_dau):
    kq, cha_map = DFS(ma_tran_dich, trang_thai_ban_dau)
    if kq is None: return
    duong_di = truy_vet_DFS(cha_map, kq)
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]


###################
def tinh_cost(ma_tran, row, col, vi_tri_dich):
    cost = 1
    
    for r, c in vi_tri_dich:
        if r == row:
            cost += abs(col - c)
            break
    return cost

#####################
def UCS(start, goal, vi_tri_dich):
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

        if np.array_equal(state, goal):
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
        cha = parent.get(key, None)  # Lấy trạng thái cha (mảng NumPy hoặc None)
        key = cha.tobytes() if cha is not None else None  # Chuyển trạng thái cha thành bytes
    return duong_di[::-1]


############################
def sinh_trang_thai_dls(ma_tran_dang_xet, hang, explored, ma_tran_cha, limit, depth):
    N = ma_tran_dang_xet.shape[0]
    trang_thai_moi = []
    if depth <= limit:  # chỉ sinh thêm nếu chưa vượt limit
        for j in range(N):
            if ma_tran_dang_xet[:, j].sum() == 0:  # cột trống
                con = ma_tran_dang_xet.copy()
                con[hang, j] = 1
                con_bytes = con.tobytes()
                if con_bytes not in explored:
                    explored.add(con_bytes)
                    ma_tran_cha[con_bytes] = ma_tran_dang_xet.tobytes()
                    trang_thai_moi.append(con)
    return trang_thai_moi


def DLS(ma_tran_dich, trang_thai_ban_dau, limit):
    stack = [(trang_thai_ban_dau, 0)]  # (state, depth)
    explored = {trang_thai_ban_dau.tobytes()}
    ma_tran_cha = {trang_thai_ban_dau.tobytes(): None}

    while stack:
        ma_tran_dang_xet, depth = stack.pop()

        # kiểm tra đích
        if np.array_equal(ma_tran_dang_xet, ma_tran_dich):
            return ma_tran_dang_xet, ma_tran_cha

        # tìm hàng đầu tiên chưa đặt xe
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


def run_DLS_generator(ma_tran_dich, trang_thai_ban_dau, limit=8):

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
    return None, {}  # không tìm thấy

def run_IDS_generator(ma_tran_dich, trang_thai_ban_dau, N=8):
    kq, cha_map = IDS(ma_tran_dich, trang_thai_ban_dau, N)
    if kq is None:
        return
    duong_di = truy_vet_DLS(cha_map, kq)  # tái sử dụng truy vết của DLS
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]

def heuristic(board):
    used_rows = set()
    used_cols = set()
    n = board.shape[0]  # vẫn lấy n để đỡ viết lại, nhưng ở đây n = 8

    for r in range(n):
        for c in range(n):
            if board[r, c] == 1:  # có quân xe
                used_rows.add(r)
                used_cols.add(c)

    # Công thức cố định cho 8x8
    return (8 - len(used_rows)) + (8 - len(used_cols))


def greedy_search(start, goal, vi_tri_dich):
    pq = []
    counter = 0
    heapq.heappush(pq, (heuristic(start), 0, counter, start.copy()))  # (h, cost, counter, state)
    visited = {start.tobytes()}
    parent = {start.tobytes(): None}
    best_cost = {start.tobytes(): 0}  # Lưu cost tốt nhất
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

        if np.array_equal(state, goal):
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

def run_greedy_generator(goal, start, vi_tri_dich, N=8):
    kq, parent, best_cost, tong_cost = greedy_search(start, goal, vi_tri_dich)
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

def A_star(start, goal, vi_tri_dich):
    pq = []
    counter = 0
    h_start = heuristic(start)
    heapq.heappush(pq, (0 + h_start, 0, counter, start.copy()))  # (f=g+h, g, counter, state)
    parent = {start.tobytes(): None}
    best_g = {start.tobytes(): 0}  # Lưu g tốt nhất cho mỗi trạng thái
    node_count = 0

    print("Bắt đầu A* SEARCH")
    print(f"Trạng thái ban đầu (g=0, h={h_start}, f={h_start}):")
    print(start)

    while pq:
        f, g, _, state = heapq.heappop(pq)
        key = state.tobytes()
        node_count += 1

        # Bỏ qua nếu trạng thái có g cao hơn g tốt nhất
        if best_g.get(key, float('inf')) < g:
            continue

        print(f"\nNode #{node_count}: g={g}, h={heuristic(state)}, f={f}")
        print("Trạng thái hiện tại:")
        print(state)

        if np.array_equal(state, goal):
            print(f"\nTÌM THẤY ĐÍCH sau {node_count} node!")
            print(f"Tổng chi phí g cuối: {g}, h=0, f={f}")
            return state, parent, best_g, g

        # Tìm hàng trống tiếp theo
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

def run_A_star_generator(goal, start, vi_tri_dich):
    kq, parent, _, g = A_star(start, goal, vi_tri_dich)
    if kq is None:
        return
    duong_di = truy_vet_A_star(parent, kq)
    print(f"Đường đi A*: {len(duong_di)} trạng thái")
    for state in duong_di:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]

  
def hill_climbing(start, goal):
    current_board = start.copy()
    current_heuristic = heuristic(current_board)
    
    path = [current_board.copy()]
    
    while True:
        neighbors = []
        n = current_board.shape[0]
        
        rook_positions = [(r, c) for r in range(n) for c in range(n) if current_board[r, c] == 1]
        
        for r, c in rook_positions:
            neighbor = current_board.copy()
            neighbor[r, c] = 0
            neighbors.append(neighbor)
        
        empty_positions = [(r, c) for r in range(n) for c in range(n) if current_board[r, c] == 0]
        for r, c in empty_positions:
            neighbor = current_board.copy()
            neighbor[r, c] = 1
            neighbors.append(neighbor)
        
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
            neighbor_heuristic = heuristic(neighbor)
            if neighbor_heuristic < best_heuristic:
                best_heuristic = neighbor_heuristic
                best_neighbor = neighbor
        
        if best_heuristic >= current_heuristic or np.array_equal(best_neighbor, goal):
            if best_heuristic < current_heuristic:
                path.append(best_neighbor.copy())
            break
        
        current_board = best_neighbor
        current_heuristic = best_heuristic
        path.append(current_board.copy())
    
    return path

def run_hill_climbing_generator(goal, start):
    path = hill_climbing(start, goal)
    for state in path:
        yield [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]

 

######################################
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
run_bfs=None; cap_nhat_bfs=[]
run_dfs=None; cap_nhat_dfs=[]
run_ucs=None; cap_nhat_ucs=[]
run_dls=None; cap_nhat_dls=[]
run_ids=None; cap_nhat_ids=[]
run_greedy=None; cap_nhat_greedy=[]
run_a_star = None;cap_nhat_a_star = []
run_hill = None;cap_nhat_hill = []



clock=pygame.time.Clock()
step_delay=1500; last_step_time=pygame.time.get_ticks()
rong_ban=kt_ban*kt_hvuong*2+khoang_cach_2ban; dai_ban=kt_ban*kt_hvuong

while True:
    vi_tri_chuot=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT: pygame.quit(); sys.exit()
        if dang_xet=="menu" and event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            x,y=vi_tri_chuot
            if 200<=x<=500 and 100<=y<=150: 
                thuat_toan="BFS"; vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                run_bfs=run_BFS_generator(Ma_Tran_Dich,Trang_Thai_Mang)
                dang_xet="game"
            elif 200<=x<=500 and 180<=y<=230: 
                thuat_toan="DFS"; vi_tri_xe=xep_phai()
                Ma_Tran_Dich=np.zeros((8,8),dtype=int)
                for (r,c) in vi_tri_xe: Ma_Tran_Dich[r][c]=1
                Trang_Thai_Mang=np.zeros((8,8),dtype=int)
                run_dfs=run_DFS_generator(Ma_Tran_Dich,Trang_Thai_Mang)
                dang_xet="game"

            elif 200 <= x <= 500 and 260 <= y <= 310:  
                thuat_toan = "UCS"
                vi_tri_xe = xep_phai()
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)

                kq, parent, visited, tong_cost = UCS(Trang_Thai_Mang, Ma_Tran_Dich, vi_tri_xe)
                print("Tổng chi phí UCS =", tong_cost)  

                duong_di = truy_vet_UCS(parent, kq)
                run_ucs = iter([
                    [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]
                    for state in duong_di
                ])
                cap_nhat_ucs = []
                dang_xet = "game"
            elif 200 <= x <= 500 and 340 <= y <= 390:  
                thuat_toan = "DLS"
                vi_tri_xe = xep_phai()
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int) 
                run_dls = run_DLS_generator(Ma_Tran_Dich, Trang_Thai_Mang, limit=8)
                cap_nhat_dls = []
                dang_xet = "game"


            elif 200 <= x <= 500 and 420 <= y <= 470:  
                thuat_toan = "IDS"
                vi_tri_xe = xep_phai()
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)  # ✅ ban đầu rỗng
                run_ids = run_IDS_generator(Ma_Tran_Dich, Trang_Thai_Mang, N=8)
                cap_nhat_ids = []
                dang_xet = "game"

            elif 200 <= x <= 500 and 500 <= y <= 550:
                thuat_toan = "GREEDY"
                vi_tri_xe = xep_phai()
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)
                print("vi_tri_dich:", vi_tri_xe)  # Debug đích
                kq, parent, visited, tong_cost = greedy_search(Trang_Thai_Mang, Ma_Tran_Dich, vi_tri_xe)
                print("Tổng chi phí GREEDY =", tong_cost)
                run_greedy = run_greedy_generator(Ma_Tran_Dich, Trang_Thai_Mang, vi_tri_xe, N=8)  # Thêm vi_tri_dich
                cap_nhat_greedy = []
                dang_xet = "game"

            elif 200 <= x <= 500 and 580 <= y <= 630:
                thuat_toan = "A*"
                vi_tri_xe = xep_phai()
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)
                kq, parent, visited, tong_cost = A_star(Trang_Thai_Mang, Ma_Tran_Dich, vi_tri_xe)
                print("Tổng chi phí A* =", tong_cost)
                duong_di = truy_vet_A_star(parent, kq)
                run_a_star = iter([
                    [(r, c) for r in range(state.shape[0]) for c in range(state.shape[1]) if state[r, c] == 1]
                    for state in duong_di
                ])
                cap_nhat_a_star = []
                dang_xet = "game"

            elif 600 <= x <= 900 and 340 <= y <= 390:  # đổi lại tọa độ của button
                thuat_toan = "HILL CLIMBING"
                vi_tri_xe = xep_phai()
                Ma_Tran_Dich = np.zeros((8, 8), dtype=int)
                for (r, c) in vi_tri_xe:
                    Ma_Tran_Dich[r][c] = 1
                Trang_Thai_Mang = np.zeros((8, 8), dtype=int)
                run_hill = run_hill_climbing_generator(Ma_Tran_Dich, Trang_Thai_Mang)
                cap_nhat_hill = []
                dang_xet = "game"






                

        elif dang_xet=="game" and event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            dang_xet="menu"

    screen.blit(nen,(0,0))
    if dang_xet=="menu":
        ve_button("BFS",200,100,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("DFS",200,160,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("UCS",200,220,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("DLS",200,280,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("IDS",200,340,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("GREEDY",200,400,300,50,(255,253,181),(150,150,150),vi_tri_chuot)
        ve_button("A*",200,460,300,50,(255,253,181),(150,150,150),vi_tri_chuot)

        # Đẩy HILL CLIMBING sang phải, ví dụ x=600
        ve_button("HILL CLIMBING", 600, 340, 300, 50, (255, 253, 181), (150, 150, 150), vi_tri_chuot)




        
    elif dang_xet=="game":
        now=pygame.time.get_ticks()
        if thuat_toan=="BFS":
            if now-last_step_time>step_delay:
                try: cap_nhat_bfs=next(run_bfs)
                except: pass
                last_step_time=now
            x_ban=(win_rong-rong_ban)//2; y_ban=(win_dai-dai_ban)//2
            ve_ban_co(x_ban,y_ban,cap_nhat_bfs)
            ve_ban_co(x_ban+kt_ban*kt_hvuong+khoang_cach_2ban,y_ban,vi_tri_xe)
        elif thuat_toan=="DFS":
            if now-last_step_time>step_delay:
                try: cap_nhat_dfs=next(run_dfs)
                except: pass
                last_step_time=now
            x_ban=(win_rong-rong_ban)//2; y_ban=(win_dai-dai_ban)//2
            ve_ban_co(x_ban,y_ban,cap_nhat_dfs)
            ve_ban_co(x_ban+kt_ban*kt_hvuong+khoang_cach_2ban,y_ban,vi_tri_xe)
        elif thuat_toan == "UCS":
            if now - last_step_time > step_delay:
                try: cap_nhat_ucs = next(run_ucs)
                except: pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2; y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_ucs)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)
        elif thuat_toan == "DLS":
            if now - last_step_time > step_delay:
                try: cap_nhat_dls = next(run_dls)
                except: pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2; y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_dls)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "IDS":
            if now - last_step_time > step_delay:
                try: cap_nhat_ids = next(run_ids)
                except: pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2; y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_ids)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "GREEDY":
            if now - last_step_time > step_delay:
                try: cap_nhat_greedy = next(run_greedy)
                except: pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2; y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_greedy)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)

        elif thuat_toan == "A*":
            if now - last_step_time > step_delay:
                try:
                    cap_nhat_a_star = next(run_a_star)
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
                    cap_nhat_hill = next(run_hill)
                except:
                    pass
                last_step_time = now
            x_ban = (win_rong - rong_ban) // 2
            y_ban = (win_dai - dai_ban) // 2
            ve_ban_co(x_ban, y_ban, cap_nhat_hill)
            ve_ban_co(x_ban + kt_ban * kt_hvuong + khoang_cach_2ban, y_ban, vi_tri_xe)





    pygame.display.update(); clock.tick(30)
