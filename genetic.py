
import numpy as np
import random

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

    print("Bắt đầu GENETIC SEARCH")
    print(f"Số cá thể ban đầu: {so_ca_the}, Xác suất đột biến: {xac_suat_dot_bien}\n")

    for the_he in range(max_the_he):
     
        fitness = [tinh_fitness(ca_the, Ma_Tran_Dich) for ca_the in quan_the]

        best_idx = np.argmax(fitness)
        best_ca_the = quan_the[best_idx]
        lich_su.append(best_ca_the.copy())

        print(f"Thế hệ {the_he+1}: fitness tốt nhất = {fitness[best_idx]}/{N}")
        print("Cá thể tốt nhất:", best_ca_the)

       
        if fitness[best_idx] == N:
            print(f" Đạt trạng thái đích sau {the_he+1} thế hệ!")
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

    print(f"\n Không tìm thấy kết quả sau {max_the_he} thế hệ.")
    return None, lich_su

def tu_dong_Genetic(Ma_Tran_Dich, N=8):
    kq, lich_su = genetic_search(Ma_Tran_Dich, N)
    if kq is None:
        return

    print(f"\nĐường đi GENETIC: {len(lich_su)} thế hệ\n")
    for ca_the in lich_su:
        yield [(r, ca_the[r]) for r in range(N)]

class Genetic:
    def __init__(self, goal_matrix):
        self.goal = goal_matrix

    def generator(self):
        return tu_dong_Genetic(self.goal)
