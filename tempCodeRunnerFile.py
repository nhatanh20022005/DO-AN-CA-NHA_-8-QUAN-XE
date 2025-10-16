def tinh_cost(ma_tran, row, col, vi_tri_dich):
    """
    Tính chi phí cho việc đặt xe tại (row, col).
    - Nếu cùng hàng/cột đã có xe → phạt thêm.
    - Càng xa cột mục tiêu của hàng này → chi phí càng lớn.
    """
    cost = 0
    n = ma_tran.shape[0]

    # Nếu hàng hoặc cột đã có xe → phạt
    for i in range(n):
        if ma_tran[row][i] == 1 or ma_tran[i][col] == 1:
            cost += 2

    # Xác định cột mục tiêu cho hàng này
    muc_tieu = [c for (r, c) in vi_tri_dich if r == row]
    if muc_tieu:
        col_goal = muc_tieu[0]
        cost += abs(col - col_goal)

    return cost