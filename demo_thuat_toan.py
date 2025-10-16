
import numpy as np
import random

# Hàm heuristic của bạn
def heuristic(board):
    used_rows = set()
    used_cols = set()
    n = board.shape[0]  # n = 8
    for r in range(n):
        for c in range(n):
            if board[r, c] == 1:  # có quân xe
                used_rows.add(r)
                used_cols.add(c)
    return (8 - len(used_rows)) + (8 - len(used_cols))

# Tạo trạng thái ban đầu: ma trận 8x8 với 0-8 xe ngẫu nhiên
def create_state(n=8):
    board = np.zeros((n, n), dtype=int)
    num_rooks = random.randint(0, n)  # Số xe ngẫu nhiên từ 0 đến 8
    positions = random.sample([(r, c) for r in range(n) for c in range(n)], num_rooks)
    for r, c in positions:
        board[r, c] = 1
    return board

# Tạo trạng thái lân cận: thêm, xóa, hoặc di chuyển xe
def get_neighbors(board):
    n = board.shape[0]  # n = 8
    neighbors = []
    
    # Tìm các vị trí có xe
    rook_positions = [(r, c) for r in range(n) for c in range(n) if board[r, c] == 1]
    
    # 1. Xóa một xe
    for r, c in rook_positions:
        neighbor = board.copy()
        neighbor[r, c] = 0
        neighbors.append(neighbor)
    
    # 2. Thêm một xe vào ô trống
    empty_positions = [(r, c) for r in range(n) for c in range(n) if board[r, c] == 0]
    for r, c in empty_positions:
        neighbor = board.copy()
        neighbor[r, c] = 1
        neighbors.append(neighbor)
    
    # 3. Di chuyển một xe sang ô trống trong cùng hàng hoặc cột
    for r, c in rook_positions:
        # Di chuyển trong cùng hàng
        for new_c in range(n):
            if new_c != c and board[r, new_c] == 0:
                neighbor = board.copy()
                neighbor[r, c] = 0
                neighbor[r, new_c] = 1
                neighbors.append(neighbor)
        # Di chuyển trong cùng cột
        for new_r in range(n):
            if new_r != r and board[new_r, c] == 0:
                neighbor = board.copy()
                neighbor[r, c] = 0
                neighbor[new_r, c] = 1
                neighbors.append(neighbor)
    
    return neighbors

# Thuật toán Hill Climbing
def hill_climbing():
    # Bắt đầu với trạng thái ngẫu nhiên
    current_board = create_state()
    current_heuristic = heuristic(current_board)
    
    while True:
        # Lấy các trạng thái lân cận
        neighbors = get_neighbors(current_board)
        # Tìm lân cận có heuristic thấp nhất
        best_neighbor = current_board
        best_heuristic = current_heuristic
        
        for neighbor in neighbors:
            neighbor_heuristic = heuristic(neighbor)
            if neighbor_heuristic < best_heuristic:
                best_heuristic = neighbor_heuristic
                best_neighbor = neighbor
        
        # Nếu không tìm được lân cận nào tốt hơn, dừng
        if best_heuristic >= current_heuristic:
            break
        
        # Cập nhật trạng thái hiện tại
        current_board = best_neighbor
        current_heuristic = best_heuristic
    
    return current_board, current_heuristic

# In bàn cờ
def print_board(board):
    for row in board:
        print(' '.join(['R' if x == 1 else '.' for x in row]))

# Chạy chương trình
if __name__ == "__main__":
    solution, solution_heuristic = hill_climbing()
    print("Kết quả tìm được:")
    print_board(solution)
    print("Heuristic:", solution_heuristic)
    if solution_heuristic == 0:
        print("Giải pháp tối ưu: Mỗi hàng và cột có đúng một con xe!")
    else:
        print("Chưa tối ưu: Còn hàng hoặc cột chưa có xe.")
