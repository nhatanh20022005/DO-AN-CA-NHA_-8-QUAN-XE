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
# simulated giống HILL, khác chỗ công thức để nó thoát khỏi vùng cục bộ
#BEAM:( xài heu) giống BFS, xét k ứng viên tốt nhất, cho chọn k cái tốt nhất
# xuất đường đi từ tt bắt đầu tới mục tiêu





### TÌM KIẾM THỎA MÃN RÀNG BUỘC (CSP)
# Phải xác định khởi tao ( đầu vào) đủ 3 tập sau:(2 tập đầu random để đúng với backtracking)
# Tập biến: X = {X1, X2, X3}

# Tập giá trị của biến( tập các vị trí của từng biến, x1,x2,x3 như nhau)
# x1={0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}
# x2={0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}
# x3={0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}

# Tập các ràng buộc( mục tiêu được thể hiện ở đây)

# lời giải: use thuật toán (backtracking, forward checking, AC-3, thực ra đều từ backtracking)để gán giá trị cho tất cả các biến thỏa mãn ràng buộc
# backtracking: chọn, thử, sai, quay lui
# thất bại: chỉ cần 1 biến gán ko thỏa ràng buộc ( ko tìm thấy lời giải)
##### Cải thiện ở 2 bước:
# ở bước chọn biến: có thể chọn biến nào dễ dẫn tới mục tiêu nhanh ko
# ở bước gán giá trị: có thể chọn giá trị nào dễ dẫn tới mục tiêu nhanh ko

##### Kỹ thuật Forward checking ( giảm miền giá trị cho các biến chưa được xét, dựa vào ràng buộc để xét các vị trí hàng i, cột j của biến trước đó, bỏ hàng i và cột j đó đi)
# sau khi gán giá trị cho 1 biến, loại bỏ các giá trị khỏi tập giá trị
# để Forward checking sau bước KIỂM TRA RÀNG BUỘC

# sau buổi này làm: tìm kiếm trong mt nhìn thấy 1 phần; backtracking và forward checking  trong CSP          
# tìm hỉu AC-3 ( ARC Consistency 3) ( thuật toán duy trì tính nhất quán của cung, cải tiến của forward checking)

# trong phần readme: từng nhóm tt thì trình bày làm cái nào, mỗi lần chạy tt thĩ xuất ảnh gif đưa lên đó